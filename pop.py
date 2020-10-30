#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:13:58 2020

@author: ANANTHA KRISHNAN O M
"""

import random as rn


def atm(bal,pn):
    restart=('Y')
    chance=3
    balance=bal
    yield balance
    
    while chance>=0:
        pin=int(input("Please Enter your PIN code: \n"))
        if pin == pn:
            print("You pin looks cool ! \n")
            while restart not in ('n', 'N', 'NO', 'no'):
                print('Press 1 for BALANCE \n')
                print('Press 2 for WITHDRAWAL\n')
                print('Press 3 for PAY \n')
                print('Press 4 for REMOVE THE CARD \n')
                opt=int(input(" \n What would you like to choose: "))
                
                if opt ==1:
                    print("\n Your BALANCE is: ", bal)
                    
    
    


bal=int(rn.randrange(5000,100000))
pn=1234
print(" Welcome to POPCORN ATM")

