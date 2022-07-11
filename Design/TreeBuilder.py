"""
1628. Design an Expression Tree With Evaluate Function

Given the postfix tokens of an arithmetic expression, build and return the binary expression tree that represents this expression.

Postfix notation is a notation for writing arithmetic expressions in which the operands (numbers) appear before their operators. For example, the postfix tokens of the expression 4*(5-(7+2)) are represented in the array postfix = ["4","5","7","2","+","-","*"].

The class Node is an interface you should use to implement the binary expression tree. The returned tree will be tested using the evaluate function, which is supposed to evaluate the tree's value. You should not remove the Node class; however, you can modify it as you wish, and you can define other classes to implement it if needed.

A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (numbers), and internal nodes (nodes with two children) correspond to the operators '+' (addition), '-' (subtraction), '*' (multiplication), and '/' (division).

It's guaranteed that no subtree will yield a value that exceeds 109 in absolute value, and all the operations are valid (i.e., no division by zero).

Follow up: Could you design the expression tree such that it is more modular? For example, is your design able to support additional operators without making changes to your existing evaluate implementation?
"""

import abc
from abc import ABC, abstractmethod
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self):
        pass

class BinaryNode(Node):
    """base class for binary nodes"""
    def __init__(self, _left, _right):
        self.left = _left
        self.right = _right
    def evaluate(self):
        pass


class Plus(BinaryNode):
    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()

class Minus(BinaryNode):
    def evaluate(self):
        return self.left.evaluate() - self.right.evaluate()

class Mul(BinaryNode):
    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()

class Div(BinaryNode):
    def evaluate(self):
        return self.left.evaluate() // self.right.evaluate()

class Num(Node):
    def __init__(self, _value):
        self.value = _value
    def evaluate(self):
        return self.value

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix):
        operators = {'+': Plus, '-': Minus, '*': Mul, '/': Div}
        stk = []
        for token in postfix:
            if token in operators:
                R = stk.pop()
                L = stk.pop()
                stk.append(operators[token](L, R))
            else:
                stk.append(Num(int(token)))
        return stk[0]





