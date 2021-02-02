#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 15:12:52 2021

@author: fabre
"""

from tree_node import TreeNode
from tree import Tree


if __name__ == "__main__":

    n0 = TreeNode("Root")
    n1 = TreeNode('N1')
    n2 = TreeNode('N2')
    n3 = TreeNode('N3')
    n0.right = n1
    n0.left = n2
    n1.left = n3

    #print(n1.is_leaf())
    #TreeNode.print_tree(n0)

    tree_display = Tree(n0)
    tree_display.transversal_deep()

    tree_display.add_node("NEW", n3)
    tree_display.transversal_deep()
    # tree_display.add_node("another_node", n1)
    # tree_display.transversal_deep()

    tree_display.remove_node(n1)
    tree_display.transversal_deep()
    tree_display.remove_node(n2)
    tree_display.transversal_deep()
