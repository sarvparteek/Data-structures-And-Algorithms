__author__ = 'sarvps'

'''
    Author: Sarv Parteek Singh
    Course: CISC 610
    Term: Late Summer
    Data Structures & Algorithms by Miller
    Stack assignment, Problem 1
    Brief: Validate an input html sequence (by just looking at opening and closing tags)
    References: Sections 3.5,3.7 from Miller
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


def htmlValidator(symbolList):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolList) and balanced:
        symbol = symbolList[index]
        if symbol == '<':
            s.push(symbol)
        elif symbol == '>':
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
    if open == '<' and close == '>':
        return True
    else:
        return False


# Insert the html text into a list. For simplification, it is done by merging three lists
htmlCheck = list('<!DOCTYPE html><html><body><h2>The title attribute</h2><p title="I')
htmlCheck.append("'")
htmlCheck += list(
    'm atooltip">Mouse over this paragraph, to display the title attribute as atooltip.</p></body></html>')
print(htmlValidator(htmlCheck))