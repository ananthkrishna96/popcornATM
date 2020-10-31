#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 20:57:27 2020

@author: ANANTHA KRISHNAN O M
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:13:58 2020

@author: ANANTHA KRISHNAN O M
"""

import random as rn
import csv


def atm(bal):
    restart=['Y','y','Yes','yes']
    temp=restart
    mon=[50,100,200,500,2000]
    chance=1
    tempbalance=bal
    balance=bal
    
    pn=0
   
    
    while chance>0:
        pin=input("\n Please Enter your PIN code: ")
        with open("namepin.csv", 'r') as file:
            file = csv.DictReader(file)
            for acc in file:
                if pin == acc['pin']:
                   pn=acc['pin']
                   print('\n \n Welcome ',acc['name'], 'You pin looks cool ! \n \n ')
        if pin == pn:
            
            while restart not in ('n', 'N', 'NO', 'no'):
                print('Press 1 for BALANCE \n')
                print('Press 2 for WITHDRAWAL\n')
                print('Press 3 for PAY \n')
                print('Press 4 for REMOVE THE CARD \n')
                opt=int(input(" \n What would you like to choose: "))
                
                if opt ==1:
                    if tempbalance == balance:
                        print("\n Your BALANCE is: ", tempbalance)
                    else:
                        print("\n Your BALANCE is: ", balance)
                    x=input(" \n Go Back ?: ")
                    if not x in restart:
                        print(" Thank You !")
                        chance-=1
                        break
                elif opt == 2:
                   
                    print(" \n \n Please Choose Denominations of 50, 100, 200, 500, 2000")
                    withdraw=float(input(" \n Enter the amount to withdraw: "))
                    if withdraw in mon:
                        balance=balance-withdraw
                        print(" \n Your New  BALANCE is: ", balance)
                    x=input(" \n Go Back ?: ")
                    if  not x  in restart:
                            print(" \n Thank You !")
                            chance-=1
                            break
                    elif withdraw not in mon:
                        print("\n Invalid amount !")
                        restart=temp
                elif opt ==3:
                    py=float(input(("\n  How Much to PAY: ")))
                    balance+=py
                    print(" \n Your BALANCE is: ", balance)
                    x=input(" \n Go Back ?: ")
                    if x not in restart:
                        print(" \n Thank You !")
                        chance-=1
                        break
                    
                elif opt==4:
                    print("\n Your Card is Removed \n Thank You !")
                    
                    restart!=temp
                    chance-=1
                    break
                else:
                    print("\n Choose Correct Option  !")
                    restart=temp
        elif pin != pn:
            print("\n Incorrect Password !")
            chance-=1
            if chance==0:
                print("\n No more tries  !")
                break
    
b=int(rn.randrange(5000,100000))


print(" \n \n Welcome to POPCORN ATM")
atm(b)

