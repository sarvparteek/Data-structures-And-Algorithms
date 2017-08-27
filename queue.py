__author__ = 'sarvps'

'''
    Author: Sarv Parteek Singh
    Course: CISC 610
    Term: Late Summer
    Data Structures & Algorithms by Miller
    Quiz 1, Problem 3
'''

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def getQueue(self):
        return self.items


def main():  # for testing
    q = Queue()
    q.enqueue('dog')
    print(q.getQueue())
    q.enqueue('cat')
    print(q.getQueue())
    q.enqueue(3)
    print(q.getQueue())
    q.dequeue()
    print(q.getQueue())


    # main() #Uncomment to enable testing