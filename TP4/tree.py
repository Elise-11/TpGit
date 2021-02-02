#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 15:02:20 2021

@author: fabre
"""
from tree_node import TreeNode

class Tree:
    '''
    This class sets up methods to perform actions on tree
    formed from nodes of the TreeNodes class.
    '''

    def __init__(self, root_node):
        '''
        Parameters
        ----------
        root_node : first tree node
        '''
        self.root_node = root_node


    def transversal_deep(self):
        '''
        Function to print the tree starting from the leaves and going up
        '''
        print(self.root_node)


    def add_node(self, added_node, target_node):
        '''
        This function allows to add a new node on a target node
        if it has at least one empty child

        Parameters
        ----------
        added_node : node we want to add
        target_node : node on which we want to add the new node
        '''
        # If the tree doesn't exist, the root takes added_node data
        added_node = TreeNode(added_node)
        if self.root_node is  None:
            self.root_node = Tree(added_node)
        #If the target_node is not a leaf and hasn't a left child
        #Left child takes added_node value
        elif target_node.is_leaf is False:
            if target_node.left is None:
                target_node.left = added_node

        #else, if ih hasn't right child
        #Right child takes added_node value
        else:
            if target_node.right is None:
                target_node.right = TreeNode(added_node)
            #else call the function starting with
            #the right child of the target node
            else:
                self.add_node(added_node, target_node.right)


    def remove_leaf(self, target_node):
        '''
        This function allows to delete a node when it's a leaf

        Parameters
        ----------
        target_node : node we want to delete
        '''
        if target_node is None:
            return
        #else:
            # if the target node is a leaf it takes None as a value
        if target_node.is_leaf:
            target_node.data = None


    def remove_node(self, target_node):
        '''
        This method allows to delete a node
        (but not by its data)

        Parameters
        ----------
        target_node : node we want to delete
        '''
        if target_node == self.root_node:
            print('This node is the root, impossible to delete it !')

        elif target_node.is_leaf is True:
            self.remove_leaf(target_node)


        else:
            #if the target node has a right child it takes its data
            #else it takes the left child data
            if target_node.right is not None:
                target_node.data = target_node.right
                target_node.right = None
            else:
                target_node.data = target_node.left
                target_node.left = None
