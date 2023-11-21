#!/usr/bin/python3
"""Singly linked list"""


class Node:
    """Class describing a Node

    Attributes:
        __data (int): Data in Node
        __next_node (Node): Next Node
    """

    def __init__(self, data, next_node=None):
        """Instantiates new node.

        Args:
            data (int): Data in node
            next_node (Node): Next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Used to get and set data in node"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Pointer to next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class describing a Singly linked list"""

    def __init__(self):
        """Instantiates new list"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts new node to a list.

        Args:
            value (Node): New node to be added
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Makes the list printable."""
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return ('\n'.join(result))
