# coding=utf-8
#---------------------------------------------------------------------------
# Copyright 2011 utahta
#---------------------------------------------------------------------------
from bs4 import BeautifulSoup
import logging
import six
import requests

def html_parser(html):
    try:
        soup = BeautifulSoup(html)
    except:
        soup = BeautifulSoup(html, "html5lib")
    return soup

def use_debug():
    logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s][%(levelname)s] %(message)s")

def debuglog(val):
    logging.debug(val)
    
def to_utf8(val):
    if isinstance(val, six.text_type):
        return val.encode("utf-8")
    else:
        return val

def to_unicode(val):
    try:
        if isinstance(val, six.binary_type):
            return val.decode('utf-8')
    finally:
        return val

def create_session():
    return requests.Session()