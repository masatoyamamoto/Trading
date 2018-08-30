# this is a program to analyze fantasy football

from configure import *

class clientKeys(object):
    def __init__(self,client_id,client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def scores(self):