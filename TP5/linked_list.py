#!/usr/bin/env python3
# coding: utf-8
"""
Created on Wed Feb  3 15:48:25 2021

@author: fabre
"""

class Node:
    """ Node of a list, it allows to create
    a node containing a data and a link """
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    """ Linked list, this class contains methods
    to manipulate linked list"""
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None and len(nodes) != 0:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next


    def empty_list(self):
        """If head doesn't exist, the list is empty and it returns True"""
        return not self.head


    def get(self, index):
        """If the head node is empty raise an exception"""
        if self.head is None:
            raise Exception('List is empty')
        self.recurs(index, self.head)


    def recurs(self, index, node):
        """Recursive function to find a node according to an
        index compared to another node """
        print(index, node)
        if node is None:
            return node
        if index == 0:
            return node
        return self.recurs(index-1, node.next)


    def add_after(self, data, new_node):
        """Function to add a new node after a given node"""
        if not self.head:
            raise Exception("List is empty")

        for node in self:
            if node.data == data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '{}' not found".format(data))

    def add_before(self, data, new_node):
        """Function to add a new node before a given node"""
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == data:
            return self.add_first(new_node)


        prev_node = self.head

        for node in self:
            if node.data == data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '{}' not found".format(data))

    def remove_node(self, data):
        """Function to remove any node"""
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '{}' not found".format(data))


    def add_first(self, node_to_add):
        """Function to add a node at the first position of the linked list"""
        node_to_add.next = self.head
        self.head = node_to_add


    def add_last(self, node_to_add):
        """Function to add a node at the last position of the linked list"""
        if self.head is None:
            self.head = node_to_add
            return

        node = self.head
        # while node.next is not None:*
        while node.next is not None:
            node = node.next
        node.next = node_to_add


    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        #return "a"
        return "{}".format(nodes)


    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
