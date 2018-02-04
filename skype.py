# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 13:04:49 2017

@author: acer
"""
from skpy import Skype
from getpass import getpass
Skype("pandey.divyanshu34", getpass(), ".tokens-pandey.divyanshu34")
sk = Skype(connect=False)
print(sk.contacts)