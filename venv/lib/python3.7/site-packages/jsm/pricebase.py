# coding=utf-8
# ---------------------------------------------------------------------------
# Copyright 2011 utahta
# ---------------------------------------------------------------------------
import datetime


def _datetime(val):
    if isinstance(val, datetime.datetime):
        return val
    try:
        return datetime.datetime.strptime(val, '%Y年%m月%d日')
    except ValueError:
        return datetime.datetime.strptime(val, '%Y年%m月')
    except:
        raise  # 発生した例外をそのままリレー


def _int(val):
    """文字列を数値オブジェクトに変換
    カンマがあったら取り除く（5,400とかのやつ）
    """
    if type(val) == int:
        return val
    if type(val) == str:
        return _numeric(val.replace(',', ''))
    return _numeric(val.decode("utf8").replace(',', ''))


def _numeric(val):
    try:
        return int(val)
    except ValueError:
        return round(float(val), 1)


class PriceData(object):
    """株価データ:
    date: 日時
    open: 初値
    high: 高値
    low: 安値
    close: 終値
    volume: 出来高
    """

    def __init__(self, date, open, high, low, close, volume, adj_close):
        self.date = _datetime(date)  # 日時
        self.open = _int(open)  # 初値
        self.high = _int(high)  # 高値
        self.low = _int(low)  # 安値
        self.close = _int(close)  # 終値
        self.volume = _int(volume)  # 出来高
        self._adj_close = _int(adj_close)  # 調整後終値（株式分割後など）
        self._adjust()

    def _adjust(self):
        """株式分割を考慮
        adj_closeが分割後の終値
        """
        rate = self.close / self._adj_close
        if rate > 1:
            self.open /= rate
            self.high /= rate
            self.low /= rate
            self.close /= rate
            self.volume *= rate

    def __repr__(self):
        """デバッグ文字列
        """
        return "<date:%s open:%s high:%s low:%s close:%s volume:%s _adj_close:%s>" % (
            self.date, self.open, self.high, self.low, self.close, self.volume, self._adj_close)


class FundPriceData(object):
    """株価データ:
    date: 日時
    price: 基準価格
    net_asset: 総純資産
    """

    def __init__(self, date, price, net_asset):
        self.date = _datetime(date)  # 日時
        self.price = _int(price)  # 基準価格
        self.net_asset = _int(net_asset)  # 総純資産

    def __repr__(self):
        """デバッグ文字列
        """
        return "<date:{0} price:{1} net_asset:{2}>".format(self.date, self.price, self.net_asset)
