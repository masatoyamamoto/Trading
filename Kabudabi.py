from configure import *
from TradeDerPy import TradeDerPy

account = {
    "username": Tredabi_USERNAME,
    "password": Tredabi_PASSWORD,
}

config = {
    "headless": True,
    "debug": True,
    "driverPath": "./venv/chromedriver"
}

td = TradeDerPy(account, config)
td.open()
td.login()

td.showHold()

td.getSuggested()

td.close()
