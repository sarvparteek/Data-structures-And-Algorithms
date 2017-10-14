__author__ = 'sarvps'

'''
    Author: Sarv Parteek Singh
    Course: CISC 610
    Term: Late Summer
    Final exam, Problem 3
    Brief: Check whether paranthesis in an expression are balanced
'''

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def paranthesisChecker(symbolList):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolList) and balanced:
        symbol = symbolList[index]
        if symbol == '(':
            s.push(symbol)
        elif symbol == ')':
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    if open == '(' and close == ')':
        return True
    else:
        return False

inputList = list('(())((())()')
print(paranthesisChecker(inputList))