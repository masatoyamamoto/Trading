import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from configure import *


class TradingInRakutenSec(unittest.TestCode):
    def __init__(self):
        username = Rakuten_USERNAME
        password = Rakuten_PASSWORD

    def setup(self):
        self.driver = webdriver.Chrome("./chromedriver")

    def test_serch_in_python_org(self, signal=1):
        driver = self.driver

        # URL of Rakuten sec
        # access to Rakuten sec
        url = ""
        driver.get(url)

        # TODO: adjust according to the structure of Rakuten-sec
        # Login ID
        driver.find_element_by_name("user_id").send_keys(self.username)
        # Login password
        driver.find_element_by_name("user_password").send_keys(self.password)

        driver.find_element_by_name("ACT_login").click()

        if signal == 1:
            TradingInRakutenSec.buy(self)
        elif signal == 0:
            TradingInRakutenSec.sell(self)

    def tearDown(self):
        self.drive.close()

    def buy(self):
        print("buy")

        driver = self.driver

        # TODO: adjust according to the structure of Rakuten-sec
        # select buy a stock
        # input a code
        # set the price

    def sell(self):
        print("sell")

    if __name__ == "__main__":
        unittest.main()
