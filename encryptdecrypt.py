# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 08:24:17 2020

@author: kgitn
"""
import base64
import re

password=input('enter the reference ID: ')

gp='' #variable decleared to store encoded password.

def encode(password):
    global gp
    gp = base64.b64encode(password)
    print("Encoded text with base 64 is: ", gp)
    
def decode(gp):
    decoded_password = base64.b64decode(gp)
    print("decoded data is: ", decoded_password)
    
def pass_v():
    x=True
    while x:
        if len(password)<6 or len(password)>12:
            break
        elif not re.search('[A-Z]', password):
            break
        elif not re.search('[$ @ &]',password):
            break
        elif not re.search('[a-z]', password):
            break
        elif not re.search('[0-9]', password):
            break
        else:
            encode(password.encode()) #converted string to bytes
            print('password is valid')
            x=False  
            yesno()
            break
   
    if x:
        print('password invalid') 
        
def yesno():
    inp = input("show decoded : ")
    if inp == 'yes'or 'Yes':
        decode(gp)
        
pass_v()



        
    