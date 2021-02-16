#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 14:24:22 2021

@author: fabre
"""

from tkinter import Entry, Label, StringVar, Tk, Button
#from TP6_controller import AdressBook

class View(Tk):
    '''
    This class contains informations about the interface.
    '''

    def __init__(self, controller):
        '''
        Interface construction with different widgets
        '''
        #super init : View is a subclass of Tk (inheritance)
        super().__init__()
        self.title('Address Book')
        self.controller = controller

        ids = ["name", "last_name", "phone", "address", "city"]
        buttons = ["search", "insert", "clear", "delete"]

        self.widgets_labs = {}
        self.widgets_entry = {}
        self.widgets_button = {}

        i, j = 0, 0

        #creation and implementation of labels and their entries
        for idi in ids:
            lab = Label(self, text=idi)
            self.widgets_labs[idi] = lab
            lab.grid(row=i, column=0)

            var = StringVar()
            entry = Entry(self, text=var)
            self.widgets_entry[idi] = entry
            entry.grid(row=i, column=1)

            i += 1

        #creation and implementation of buttons
        for idi in buttons:
            button = Button(self, text=idi)
            self.widgets_button[idi] = button
            button.grid(row=i+1, column=j)

            j += 1

        #Label to show result
        self.label_result = Label(self, text="result of your search :", width=50, bg="azure")
        self.label_result.grid(row=7, column=1)

        #Configuration of the actions triggered by the buttons
        self.widgets_button["insert"].config(command=controller.insert_ind)
        self.widgets_button["search"].config(command=controller.search_ind)
        self.widgets_button["clear"].config(command=controller.clear_entries)
        self.widgets_button["delete"].config(command=controller.delete_ind)

    def main(self):
        '''
        Launching the interface
        '''
        self.mainloop()
