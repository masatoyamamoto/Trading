
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from configure import *


class TradingInFirsTrade():
    def __init__(self):
        self.username = Firstrade_USERNAME
        self.password = Firstrade_PASSWORD
        self.pin = Firstrade_PIN
        self.driver = webdriver.Chrome("./venv/chromedriver")

    def logIn(self, signal=1):
        driver = self.driver

        # access to FirsTrade
        url = "https://invest.firstrade.com/cgi-bin/login"
        driver.get(url)

        # Login ID
        driver.find_element_by_name("username").send_keys(self.username)
        # Login password
        driver.find_element_by_name("password").send_keys(self.password)

        # Set the destination page
        dest_page = driver.find_element_by_name("destination_page")
        dest_page_element = Select(dest_page)
        dest_page_element.select_by_value("stock_order")

        driver.find_element_by_id("loginButton").click()

        driver.find_element_by_xpath('div[@class="pin_inner"]').send_keys(self.pin)

        print(driver.title)

    def tearDown(self):
        self.driver.close()

    def buy(self, code):
        print("buy")
        driver = self.driver

        # TODO: adjust according to the structure of FirsTrade
        # select buy a stock

        # input a code
        # set the price

    def sell(self):
        print("sell")


Trd = TradingInFirsTrade()
Trd.logIn()
