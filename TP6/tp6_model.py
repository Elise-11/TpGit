#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 16:01:34 2021

@author: fabre
"""

class Individual:
    '''
    This class contains informations to be filled in
    about individuals of the adress book.
    '''

    def __init__(self, name, last_name, phone, address, city):
        '''
        Class constructor
        Informations about individuals

        Parameters
        ----------
        name : first name
        last_name : last name
        phone : phone number
        address : adress
        city : city
        '''
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.address = address
        self.city = city

    def __str__(self):
        '''
        Display formatting
        '''
        return self.name +"\t"+ self.last_name +"\t"+ self.phone + "\t"+ self.address  +"\t"+ self.city
