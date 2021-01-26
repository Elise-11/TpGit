#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 16:10:22 2021

@author: fabre
"""

from node import Node
from chained_list import ChainedList

def test_print_node():
    """
    This fucntion is specially created to understand how __str__ method of node works.
    It defines nodes and their links.
    Returns
    -------
    nodes list : chained list
    """
    node_1 = Node(1)
    node_2 = Node(3)
    node_3 = Node(11)
    #node_4 = Node(28)
    node_1.link = node_2
    node_2.link = node_3
    #node_3.link = node_4
    print(node_1)

if __name__ == "__main__":
    test_print_node()

    CL = ChainedList([1, 5, 6, 12, 34])
    print(CL)

    #test for insert_node_after function
    #insert a new node with data 28 after the node containing the data 12
    CL.insert_node_after(12, 28)
    print(CL)

    #test for delete_node function
    #delete the node containing the data 12
    CL.delete_node(12)
    print(CL)
