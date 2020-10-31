#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 12:49:16 2020

@author: ANANTHA KRISHNAN O M
"""

import random as rn
from bank import bank


print(" \n \n \n Welcome to POPCORN ATM")


bal=int(rn.randrange(5000,100000))

c=bank(bal)
c.atm()