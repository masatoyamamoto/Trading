import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from configure import *


class TradingInRakutenSec():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome("./venv/chromedriver")

    def test_serch_in_python_org(self, signal=1):
        driver = self.driver

        # URL of Rakuten sec
        # access to Rakuten sec
        url = "https://www.rakuten-sec.co.jp/ITS/V_ACT_Login.html"
        driver.get(url)

        # Login ID
        driver.find_element_by_name("loginid").send_keys(self.username)
        # Login password
        driver.find_element_by_name("passwd").send_keys(self.password)

        driver.find_element_by_id("login-btn").click()

        print(driver.title)

        # if signal == 1:
        #     TradingInRakutenSec.buy(self)
        # elif signal == 0:
        #     TradingInRakutenSec.sell(self)

    def tearDown(self):
        self.driver.close()

    def buy(self):
        print("buy")

        driver = self.driver

        # TODO: adjust according to the structure of Rakuten-sec
        # select buy a stock
        # input a code
        # set the price

    def sell(self):
        print("sell")


Trd = TradingInRakutenSec(Rakuten_USERNAME, Rakuten_PASSWORD)
Trd.test_serch_in_python_org()
Trd.tearDown()
