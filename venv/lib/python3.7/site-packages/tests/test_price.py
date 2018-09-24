# coding=utf-8
#---------------------------------------------------------------------------
# Copyright 2011 utahta
#---------------------------------------------------------------------------
import jsm
from jsm.pricebase import PriceData
from tests import CCODE

def test_get():
    q = jsm.Quotes()
    d = q.get_price(CCODE)
    assert isinstance(d, PriceData)
    assert isinstance(d.open, (int, float))
    assert isinstance(d.close, (int, float))
    assert isinstance(d.high, (int, float))
    assert isinstance(d.low, (int, float))
    assert isinstance(d.volume, int)
