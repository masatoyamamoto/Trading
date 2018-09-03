import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from configure import *


class TradingInFirsTrade():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome("./venv/chromedriver")

    def logInToRakuten(self, signal=1):
        driver = self.driver

        # access to FirsTrade
        url = "https://invest.firstrade.com/cgi-bin/login"
        driver.get(url)

        # Login ID
        driver.find_element_by_name("username").send_keys(self.username)
        # Login password
        driver.find_element_by_name("password").send_keys(self.password)

        driver.find_element_by_id("loginButton").click()

        print(driver.title)

    def tearDown(self):
        self.driver.close()

    def buy(self, code):
        print("buy")
        driver = self.driver

        # TODO: adjust according to the structure of Rakuten-sec
        # select buy a stock

        # input a code
        # set the price

    def sell(self):
        print("sell")


Trd = TradingInFirsTrade(Firstrade_USERNAME, Firstrade_PASSWORD)
Trd.logInToRakuten()
Trd.tearDown()
