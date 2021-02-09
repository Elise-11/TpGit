#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:48:25 2021

@author: fabre
"""
import unittest
#import sys
#change of folder higher
#sys.path.append("..")
from linked_list import LinkedList
from linked_list import Node


class TestLinkedList(unittest.TestCase):
    """Test case used to test methods from LinkedList class"""


    def setUp(self):
        """Test initialization"""
        self.liste = LinkedList()


    def test_newlist_empty(self):
        """2.1 test to check if a new created list is empty"""
        #print(self.liste.empty_list())
        #assertTrue checks if the empty_list() method returns True
        self.assertTrue(self.liste.empty_list())

    def test_add_notempty(self):
        """2.2 test to check that a list is not empty
        if if we've just added an element """
        new_node = Node("x")
        self.liste.add_first(new_node)
        #in this case we check that the list is not empty
        self.assertTrue(not self.liste.empty_list())


    def test_unchanged(self):
        """2.3 test if when we add and remove a new element,
        the linked list remains unchanged"""
        #list creation [a,b]
        node_a, node_b = "a", "b"
        self.liste.add_first(Node(node_a))
        self.liste.add_after(node_a, Node(node_b))
        #store the created list in a variable to be able to compared it later
        first_list = self.liste
        node_d = "d"
        self.liste.add_last(Node(node_d))
        self.liste.remove_node(node_d)
        #assertEqual checks that two given objects are equal
        self.assertEqual(self.liste, first_list)


    def test_add_first(self):
        """2.4 test if an element added at the first position of the list
        is the head of the list"""
        node_e, node_b, node_c = "e", "b", "c"
        self.liste.add_first(Node(node_b))
        self.liste.add_after(node_b, Node(node_c))
        #add the new head node e
        self.liste.add_first(Node(node_e))
        #comparison between the head of the list and the element inserted at the beginning
        self.assertEqual(self.liste.head.__repr__(), node_e)


    # def test_remain_empty(self):
    #     """3.3 test if when we add an element to an empty list,
    #     and remove this element the list remain empty"""
    #     node_first = "a"
    #     self.liste.add_first(Node(node_first))
    #     self.liste.remove_node(node_first)
    #     self.assertTrue(self.liste.empty_list())


if __name__ == '__main__':
    unittest.main()
