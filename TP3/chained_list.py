#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: fabre
"""

from node import Node

class ChainedList:
    '''
    This class sets up methods to perform actions on chained lists
    formed from nodes of the node class.
    '''
    def __init__(self, list_n):
        ''''
        This function initialize the first list position,
        the first Node takes the head list value,
        then it browses the given list to change it as a chained list
        adding link between each list values.

        Parameters
        -----------
        list_n : list we want to transfert in a chained list of Node object
        '''
        self.head = Node(list_n[0])
        current = self.head
        for val in list_n[1:]:
            current.link = Node(val)
            current = current.link


    def __str__(self):
        ''''
        This function is needed to print string representation
        of an object (and not its place in memory).
        '''
        return str(self.head)


    def insert_node_after(self, target_data: int, new_node: int):
        '''
        This function allows to insert a new node with the
        data in a chained list after the searched data node.
        Parameters
        -----------
        target_data : searched data
        new_node : node to insert
        '''
        current = self.head
        #this loop search the index of the node for the searched data
        #it stops when the data corresponds to the searched data
        while current is not None:
            if current.data == target_data:
                break
            current = current.link
        #create the new node with its value
        new_data = Node(new_node)
        #The link for the new node takes the link of the current node
        new_data.link = current.link
        #The link for the current node takes the data of the new node
        current.link = new_data



    def delete_node(self, target_data):
        '''
        This function allows to delete a node by its data(value)
        in a chained list.
        parameters
        -----------
        target_data : searched data to delete
        '''
        current = self.head
        while current is not None:
            if current.data == target_data:
                break
            #the current node becomes the next node
            previous = current
            current = current.link

        #if the searched data doesn't exist return the list
        if current is None:
            return
        #unlink the node from chained list
        previous.link = current.link


    #if we want to insert a value at the start of the list
    #we have to implement another function : insert_node_before()

    #if we want to delete the first or the last node
    #we have to implement two functions :
    #delete_first_node() and delete_last_node()
