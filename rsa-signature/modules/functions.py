#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 3 2023

@author: iluzioDev

This document contains the functions used in the project.
"""
import random
import math
from modules.constants import *

def fast_exponentiation(base, exponent, modulus):
  """Fast exponentiation algorithm.

  Args:
      base (int): Base number.
      exponent (int): Exponent number.
      modulus (int): Modulus number.
  """
  base = int(base)
  exponent = int(exponent)
  modulus = int(modulus)

  result = 1
  base = base % modulus
  while exponent > 0 and base > 1:
    if exponent % 2 == 1:
      result = (result * base) % modulus
      exponent = exponent - 1
    else:
      base = (base * base) % modulus
      exponent = exponent / 2
  return result

def euclid_extended(a, b):
  """
  Euclid's extended algorithm.

  Args:
    a (int): First number.
    b (int): Second number.

  Returns:
    tuple: Tuple containing the GCD, the x coefficient and the y coefficient.
  """
  if a == 0:
    return (b, 0, 1)
  else:
    g, y, x = euclid_extended(b % a, a)
    s = 1 if a > 0 else -1
    t = 1 if b > 0 else -1
    return (g, x - ((b // a) * y) * s, y * t)
  
def lehman_peralta(x, n = 50):
  """
  Function that implements Lehman-Peralta primality test.

  Args:
    x (int): Number to be tested.
    n (int): Number of iterations. Defaults to 10.
    
  Returns:
    bool: True if x is prime, False otherwise.
  """
  # Step 1: Check special cases.
  if x <= 1:
    return False
  elif x <= 3:
    return True
  
  maybe_prime = False
  for i in range(n):
    # Step 2: Choose a random number a in the range [2, x - 1], both inclusive.
    d = round((x - 1) / 2)
    a = random.randint(2, d)
  
    # Step 3: Compute a^(x - 1)/2 mod x.
    result = fast_exponentiation(a, d, x)
  
    # If result is x - 1, then x is **probably** prime.
    if result == x - 1:
      maybe_prime = True
  
    # Step 4: If result is 1 or -1, then x is **probably** prime.
    if result == 1 or result == x - 1:
      continue
    # If result of a^(x - 1)/2 is not 1 or -1, then x is composite.
    else:
      return False
  # If all iterations resulted in 1, then x is composite.
  return maybe_prime

def encrypt(message, e, n):
  """
  Encrypts a message using RSA algorithm.

  Args:
      message (str): Message to encrypt.
      e (int): Public exponent.
      n (int): Public modulus.

  Returns:
      str: Encrypted message.
  """
  message = ''.join([char for char in message.upper() if char in ALPHABET])
  block_size = math.floor(math.log(n, len(ALPHABET)))
  coded = []
  encrypted = []
  
  for i in range(0, len(message), block_size):
    block = message[i:i + block_size]
    if len(block) < block_size:
      block += "X" * (block_size - len(block))
    num = sum(ALPHABET.index(char) * pow(len(ALPHABET), block_size - 1 - j) for j, char in enumerate(block))
    coded.append(num)
    encrypted.append(fast_exponentiation(num, e, n))

  print('Block size: ' + str(block_size))
  print(ROW)
  print('Message: ' + message)
  print(ROW)
  print('Coded message: ' + " ".join(str(num) for num in coded))
  print(ROW)
  
  return "".join(str(num) + " " for num in encrypted)

def sign(message, e, n):
  """
  Signs a message using RSA algorithm.

  Args:
      message (str): Message to sign.
      e (int): Public exponent.
      n (int): Public modulus.

  Returns:
      str: Signed message.
  """
  message = ''.join([char for char in message.upper() if char in ALPHABET])
  block_size = math.floor(math.log(n, len(ALPHABET)))
  coded = []
  encrypted = []
  
  for i in range(0, len(message), block_size):
    block = message[i:i + block_size]
    if len(block) < block_size:
      block += "X" * (block_size - len(block))
    num = sum(ALPHABET.index(char) * fast_exponentiation(len(ALPHABET), block_size - 1 - j, n) for j, char in enumerate(block))
    coded.append(num)
    encrypted.append(fast_exponentiation(num, e, n))

  print('Block size: ' + str(block_size))
  print(ROW)
  print('Message: ' + message)
  print(ROW)
  print('Coded message: ' + " ".join(str(num) for num in coded))
  print(ROW)
  
  return "".join(str(num) + " " for num in encrypted)

def verify(message):
  """
  Decrypts a message using RSA algorithm.

  Args:
    message (str): Message to decrypt.

  Returns:
    str: Decrypted message.
  """
  decrypted = ALPHABET[int(message)]
  return decrypted
