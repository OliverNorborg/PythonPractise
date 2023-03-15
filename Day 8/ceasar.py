#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 15:16:30 2023

@author: olivernorborg
"""
from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(message, number, cryption):
    cryption_string = ""
    if cryption == "decode":
        number *= -1
    for i in range(len(message)):
        if message[i] in alphabet:
            index = alphabet.index(message[i])
            position = index + number
            if position < 0:
                position += len(alphabet)
            elif position > len(alphabet):
                position -= len(alphabet)
            cryption_string += alphabet[position]
        else:
            cryption_string += message[i]
    print(cryption_string)


conti = "yes"
while(conti =="yes"):
    direction = (input("Type 'encode' to encrypt, type 'decode' to decrypt:\n"))
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #making sure the shift if not longer than the alphabet, but incase it is
    # we subtract the length 
    while (shift > len(alphabet)):
        shift = shift%len(alphabet)
  
    ceasar(text, shift, direction)
    conti = input("Would you like to continue? Type 'yes' or 'no'\n").lower()

print("Thank you for using ceasar encryption. Have a nice day!")