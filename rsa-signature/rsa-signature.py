#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 3 2023

@author: iluzioDev

This script implements the RSA signature mode.
"""
from modules.constants import ROW
import modules.functions as functions

def main():
  """
  Main function
  """
  while True:
    print(ROW)
    print('■                 WELCOME TO THE RSA SIGNATURE MODE!                 ■')
    print(ROW)
    print('What do you want to do?')
    print('[1] Sign a message.')
    print('[2] Verify a message.')
    print('[0] Exit.')
    print(ROW)
    option = input('Option  ->  ')
    print(ROW)

    if int(option) not in range(3):
      print('Invalid option!')

    if option == '0':
      print('See you soon!')
      print(ROW)
      break
    
    if int(option) == 1:
      p = int(input('Enter a prime number (p): '))
      print(ROW)
      if not functions.lehman_peralta(p):
        print('Not a prime number!')
        continue
      q = int(input('Enter a prime number (q): '))
      print(ROW)
      if not functions.lehman_peralta(q):
        print('Not a prime number!')
        continue
      e = int(input('Enter a euler number (e): '))
      print(ROW)
      
      n = (p - 1) * (q - 1)
      mcd, d, *_ = functions.euclid_extended(e, n)
      if mcd != 1:
        print('Invalid number!')
        continue
      print('Euler\'s value: ' + str(d))
      print(ROW)
      
      message = input('Enter a message: ')
      print(ROW)
      
      signed = functions.sign(message, d, p * q)
      print('Signed message: ' + signed)
    
    if option == '2':
      message = input('Enter a message: ')
      print(ROW)
      e = int(input('Enter a euler number (e): '))
      print(ROW)
      n = int(input('Enter a modulus number (n): '))
      print(ROW)
      
      message = functions.fast_exponentiation(message, e, n)
      decoded = functions.verify(message)
      print('Decoded message: ' + decoded)     
    
if __name__ == '__main__':
  main()
