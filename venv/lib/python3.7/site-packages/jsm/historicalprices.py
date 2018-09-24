# coding=utf-8
#---------------------------------------------------------------------------
# Copyright 2011 utahta
#---------------------------------------------------------------------------
import datetime
import time
import csv
import sys
from .util import html_parser, debuglog, create_session
from .pricebase import PriceData, FundPriceData
from .exceptions import CCODENotFoundException


class HistoricalPricesParser(object):
    """過去の株価情報ページパーサ"""
    SITE_URL = "http://info.finance.yahoo.co.jp/history/"
    DATA_FIELD_NUM = 7 # データの要素数
    INDEX_DATA_FIELD_NUM = 5 # 指数系データの要素数
    FUND_FIELD_NUM = 3 # 投資信託データの要素数
    COLUMN_NUM = 50 # 1ページ辺り最大行数

    def __init__(self):
        self._elms = []
        self._session = create_session()
    
    def fetch(self, start_date, end_date, ccode, range_type, page=1):
        """対象日時のYahooページを開く
        start_date: 開始日時(datetime)
        end_date: 終了日時(datetime)
        ccode: 証券コード
        range_type: 取得タイプ（デイリー, 週間, 月間）
        page: ページ(1ページ50件に調整)
        """
        params = {'sy': start_date.year, 'sm': start_date.month, 'sd': start_date.day,
                                   'ey': end_date.year, 'em': end_date.month, 'ed': end_date.day,
                                   'p': page, 'tm':range_type, 'code':ccode}
        resp = self._session.get(self.SITE_URL, params=params)
        html = resp.text
        soup = html_parser(html)
        self._elms = soup.findAll("table", attrs={"class": "boardFin yjSt marB6"})
        if len(self._elms) == 0:
            raise CCODENotFoundException("couldn't find ccode")
        self._elms = self._elms[0].findAll("tr")[1:]
        debuglog(resp.url)
        debuglog(len(self._elms))
        
    def get(self, idx=0):
        if self._elms:
            # 有効なデータを1件取得
            if idx >= 0:
                elm = self._elms[idx]
            else:
                return None
            tds = elm.findAll("td")
            if len(tds) == self.DATA_FIELD_NUM:
                data = [self._text(td) for td in tds]
                data = PriceData(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
                return data
            elif len(tds) == self.INDEX_DATA_FIELD_NUM:
                data = [self._text(td) for td in tds]
                data = PriceData(data[0], data[1], data[2], data[3], data[4], 0, data[4])
                return data
            elif len(tds) == self.FUND_FIELD_NUM:
                data = [self._text(td) for td in tds]
                data = FundPriceData(data[0], data[1], data[2])
                return data
            else:
                return None
        else:
            return None
    
    def get_all(self):
        res = []
        for i in range(len(self._elms)):
            data = self.get(i)
            if data:
                res.append(data)
        return res

    def _text(self, soup):
        if sys.version_info.major < 3:
            return soup.text.encode("utf-8")
        else:
            return soup.text

class HistoricalPrices(object):
    """Yahooファイナンスから株価データを取得する
    """
    INTERVAL = 0.5 # 株価取得インターバル（秒）
    DAILY = "d" # デイリー
    WEEKLY = "w" # 週間
    MONTHLY = "m" # 月間
    
    def __init__(self):
        self._range_type = self.DAILY # 取得タイプ

    def get(self, ccode, page=1):
        """指定ページから一覧を取得"""
        p = HistoricalPricesParser()
        end_date = datetime.date.today()
        start_date = datetime.date(2000, 1, 1)
        p.fetch(start_date, end_date, ccode, self._range_type, page)
        return p.get_all()
    
    def get_latest_one(self, ccode):
        """最新の1件を取得"""
        p = HistoricalPricesParser()
        end_date = datetime.date.today()
        start_date = end_date - datetime.timedelta(7) # とりあえず1週間ぶん取得
        p.fetch(start_date, end_date, ccode, self._range_type, 1)
        return p.get()
    
    def get_one(self, ccode, date):
        """指定日時の中から1件を取得"""
        p = HistoricalPricesParser()
        p.fetch(date, date, ccode, self._range_type, 1)
        return p.get()
    
    def get_range(self, ccode, start_date, end_date):
        """指定日時間から取得"""
        p = HistoricalPricesParser()
        res = []
        for page in range(1,500):
            p = HistoricalPricesParser()
            p.fetch(start_date, end_date, ccode, self._range_type, page)
            data = p.get_all()
            if not data:
                break
            res.extend(data)
            time.sleep(self.INTERVAL)
        return res
        
    def get_all(self, ccode):
        """全部取得"""
        start_date = datetime.date(2000, 1, 1)
        end_date = datetime.date.today()
        res = []
        for page in range(1,500):
            p = HistoricalPricesParser()
            p.fetch(start_date, end_date, ccode, self._range_type, page)
            data = p.get_all()
            if not data:
                break
            res.extend(data)
            time.sleep(self.INTERVAL)
        return res

class HistoricalDailyPrices(HistoricalPrices):
    """デイリーの株価データを取得
    """
    def __init__(self):
        super(HistoricalDailyPrices, self).__init__()
        self._range_type = self.DAILY

class HistoricalWeeklyPrices(HistoricalPrices):
    """週間の株価データを取得
    """
    def __init__(self):
        super(HistoricalWeeklyPrices, self).__init__()
        self._range_type = self.WEEKLY

class HistoricalMonthlyPrices(HistoricalPrices):
    """月間の株価データを取得
    """
    def __init__(self):
        super(HistoricalMonthlyPrices, self).__init__()
        self._range_type = self.MONTHLY

class HistoricalPricesToCsv(object):
    """株データをCSVファイルに
    """
    def __init__(self, path, klass):
        self._path = path
        self._klass = klass
    
    def save(self, ccode, page=0):
        """指定ページから一覧をCSV形式で保存"""
        c = csv.writer(open(self._path, 'w'))
        for one in self._klass.get(ccode, page):
            c.writerow(self._csv(one))
    
    def save_latest_one(self, ccode):
        """最新の1件をCSV形式で保存"""
        c = csv.writer(open(self._path, 'w'))
        one = self._klass.get_latest_one(ccode)
        if one:
            c.writerow(self._csv(one))
    
    def save_one(self, date, ccode):
        """指定日時の中から1件をCSV形式で保存"""
        c = csv.writer(open(self._path, 'w'))
        one = self._klass.get_one(ccode, date)
        if one:
            c.writerow(self._csv(one))
    
    def save_all(self, ccode):
        """全部CSV形式で保存"""
        c = csv.writer(open(self._path, 'w'))
        for one in self._klass.get_all(ccode):
            c.writerow(self._csv(one))
    
    def _csv(self, one):
        """株データをCSV形式に変換"""
        return [one.date.strftime('%Y-%m-%d'),
                one.open, one.high, one.low, 
                one.close, one.volume]
