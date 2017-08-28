__author__ = 'sarvps'

'''
    Author: Sarv Parteek Singh
    Course: CISC 610
    Term: Late Summer
    Data Structures & Algorithms by Miller
    Quiz 1, Problem 4
    Brief: Implements a queue such that both enqueue and dequeue have O(1) performance on average. 
            In this case, it means that most of the time enqueue and dequeue will be O(1) except in one particular 
            circumstance, where dequeue will be O(n)
    References: https://stackoverflow.com/questions/69192/how-to-implement-a-queue-using-two-stacks
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

    def getStack(self):
        return self.items


class Queue:
    def __init__(self):
        self.inputStack = Stack()
        self.outputStack = Stack()

    def enqueue(self, item):
        self.inputStack.push(item)

    def dequeue(self):
        if (self.outputStack.isEmpty()):
            while (self.inputStack.isEmpty() == False):
                self.outputStack.push(self.inputStack.pop())

        retVal = None
        if (not self.outputStack.isEmpty()):
            retVal = self.outputStack.pop()

        return retVal

    def size(self):
        return self.inputStack.size() + self.outputStack.size()

    def isEmpty(self):
        return self.inputStack.isEmpty() and self.outputStack.isEmpty()

    def getQueue(self):
        qList = []
        reverseOutput = []  # Note that we can't use reverse() method since it reverses the actual list
        if (len(self.outputStack.getStack())):
            for i in range(len(self.outputStack.getStack()) - 1, -1, -1):
                reverseOutput.append(self.outputStack.getStack()[i])
        qList += reverseOutput + self.inputStack.getStack()
        return qList


def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("After enqueueing 1,2,3")
    print(q.getQueue())
    q.dequeue()
    print("After first dequeue")
    print(q.getQueue())
    q.enqueue(4)
    q.enqueue(5)
    print("After enqueueing 4,5")
    print(q.getQueue())
    q.dequeue()
    print("After dequeueing")
    print(q.getQueue())
    q.enqueue(6)
    q.enqueue(7)
    print("After enqueueing 6,7")
    print(q.getQueue())
    q.dequeue()
    print("After dequeueing")
    print(q.getQueue())

#main() #Test
