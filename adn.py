#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    documentation here
"""

__author__ = 'Elise FABRE'



def is_valid(dna_str):
    valid ='atcg'
    for letter in dna_str:
        if letter not in valid:
            return False
    return True 
    
 
def get_valid_dna() :
    while not is_valid(input("Entrer une chaîne ADN :")) :
        print("DNA chain is not valid \n please enter a new chain !")
    print("DNA chain is valid!")

get_valid_dna()

#this is a python script
