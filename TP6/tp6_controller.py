#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 08:22:27 2021

@author: fabre
"""

from tkinter import  messagebox, END
from tp6_model import Individual
from tp6_view import View


class AdressBook:
    '''
    This class contains methods of the controller
    which makes the link between the view and the model
    '''
    def __init__(self, dico, view):
        '''
        AdressBook constructor
        '''
        self.dico = dico
        self.view = View(self)


    def open_file(self):
        '''
        This function allows to open the file Adress book and read what's in it
        to put people's information in a dictionary
        '''
        with open('Adress_book.tsv', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.strip() != "":
                    line = line[:-1]

                    print(line)
                    line = line.split('\t')
                    print(line)
                    #data from the file to the dictionary
                    self.dico[line[0]] = Individual(line[0], line[1], line[2], line[3], line[4])
            file.close()
            print(self.dico)


    def write_in_file(self):
        '''
        This function allows to write in the Adress book
        '''
        with open('Adress_book.tsv', 'w') as file:
            #browse the dictionary and write it in the file
            for key in self.dico.items():
                file.write(str(self.dico[key]) + "\n")
            file.close()


    def insert_ind(self):
        '''
        This function allows to add a new individual in
        the adress book
        '''
        self.open_file()
        #create an individual
        i = Individual(self.view.widgets_entry["name"].get(),
                       self.view.widgets_entry["last_name"].get(),
                       self.view.widgets_entry["phone"].get(),
                       self.view.widgets_entry["address"].get(),
                       self.view.widgets_entry["city"].get())
        #if the entry is empty raise a warning message
        if self.view.widgets_entry["name"].get() == "":
            messagebox.showerror("Warning", "fill in the field name please ")
        #if the searched name is not in the dictionary add it with its informations
        #to the dictionnary and in the file
        elif self.view.widgets_entry["name"].get() not in self.dico:
            self.dico[self.view.widgets_entry["name"].get().lower()] = i
            self.write_in_file()
            messagebox.showinfo("Information", "The person has been registered successfully !")
            #else raise a warning message
        else:
            messagebox.showerror("warning", "The person is already registered.")
        self.clear_entries()


    def search_ind(self):
        '''
        This function allows to search for an individual
        by his/her first name
        '''
        self.open_file()
        searched_name = self.view.widgets_entry["name"].get()
        #if the individual is in the dictionnary
        #write his/her informations in a label
        if searched_name.lower() in self.dico.keys():
            self.view.label_result.config(text=str(self.dico[searched_name.lower()]))
        elif searched_name == "":
            messagebox.showerror("Warning", "Please enter a name !")
        else:
            messagebox.showerror("Warning", "No information found.")


    def clear_entries(self):
        '''
        This function allowws to clear all entries
        '''
        for entry in self.view.widgets_entry.values():
            entry.delete(0, END)


    def delete_ind(self):
        '''
        This function allows to delete an individual
        from the dictionnary and write the new dictionnary in the file
        '''
        self.open_file()
        delete_name = self.view.widgets_entry["name"].get()
        if delete_name.lower() in self.dico.keys():
            del  self.dico[delete_name.lower()]
            self.write_in_file()
            messagebox.showinfo("Information", "person well deleted")
        elif delete_name == "":
            messagebox.showerror("Warning", "Please enter a name !")
        else:
            messagebox.showerror("Warning", "No information found.")
        self.clear_entries()


    def main(self):
        '''
        Main function of the controller.
        '''
        self.view.main()


if __name__ == "__main__":
    book = AdressBook({}, View)
    book.main()
