#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:59:03 2021

@author: fabre
"""

class Node:
    """
    This class contains node attributes
    and the method to create link between nodes
    Parameters
    ----------
    nodes : list
        creating a chained list defining nodes and their links
    """

    def __init__(self, param_data: int):
        """
        Constructor : method called each time an object (a node) is created
        Parameters
        ----------
        param_data : value assigned to the node
        """
        self.data = param_data
        self.link = None


    def __str__(self):
        """
        String representation of an object(a node)
        returns
        ---------
        list : all nodes
        """
        list_nodes = []
        node = self
        #Browse the given nodes parameters, while link is not null
        #add data of the node and its link (that points to the next node) to the list
        while node.link is not None:
            list_nodes.append(node.data)
            node = node.link
        #if the link doesn't exist just add the data without link
        list_nodes.append(node.data)
        return str(list_nodes)
