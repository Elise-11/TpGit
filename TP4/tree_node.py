#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 14:46:41 2021

@author: fabre
"""

class TreeNode:
    '''
    This class contains tree nodes attributes and methods
    to create linked nodes in a binary tree
    '''

    def __init__(self, data):
        '''
        Constructor : method called each time an object (a node) is created

        Parameters
        ----------
        data : the data attributed to the node
        '''
        self.left = None
        self.right = None
        self.data = data
        self.level = 0

    def __str__(self):
        '''
        String representation of the tree

        Returns
        -------
        Created tree
        '''
        if self.is_leaf():
            return str(self.data)

        return "[" + str(self.left) +";"+ str(self.right) + "]:" + str(self.data)


    def print_tree(self):
        '''
        Print the tree :
            left branches (starting with the left leaf)
            root
            right branches (finishing with the right leaf)
        '''
        #recursive function
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()


    def is_leaf(self):
        '''
        This function allows to check if a node
        has children or not
        '''
        return self.right is None and self.left is None
