__author__ = 'sarvps'

'''
    Author: Sarv Parteek Singh
    Course: CISC 610
    Term: Late Summer
    Mid-term exam, Problem 2
    Brief: Finds capital gains/losses for a given input sequence
'''

class Queue:
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return self.elements == []

    def enqueue(self,element): #at the start of list
        self.elements.insert(0,element)

    def dequeue(self): # from the end of list
        return self.elements.pop()

    def size(self):
        return len(self.elements)

class shareQueue(Queue):
    def __init__(self,price):
        Queue.__init__(self)
        self.gains = 0
        self.expenditure = 0

    def getGains(self):
        return self.gains

    def getNetExpenditure(self):
        return self.expenditure

    def buyShares(self,shareQuantity,sharePrice):
        for i in range(shareQuantity):
            self.enqueue(sharePrice)
            self.expenditure += sharePrice

    def sellShares(self,shareQuantity,sellingPrice):
        for i in range(shareQuantity):
            self.gains += sellingPrice - self.dequeue()

    def getList(self):
        return self.elements


def handleBuying(squeue):
    res = input("Do you wish to buy shares(y/n)?\n")
    if (res != 'y' and res != 'Y'):
        return
    quantity = int(input("How many shares do you wish to buy?\n"))
    price = int(input("At what price do you wish to buy these shares?\n"))
    squeue.buyShares(quantity,price)

def handleSelling(squeue):
    res = input("Do you wish to sell shares(y/n)?\n")
    if (res != 'y' and res != 'Y'):
        return
    quantity = int(input("How many shares do you wish to sell?\n"))
    price = int(input("At what price do you wish to sell these shares?\n"))
    squeue.sellShares(quantity,price)

def showExpenditureAndGains(squeue):
    print("Your current expenditure is ${} and gains are ${}".format(squeue.getNetExpenditure(),squeue.getGains()))

q = Queue()
s = shareQueue(q)
while (True):
    handleBuying(s)
    handleSelling(s)
    showExpenditureAndGains(s)
    res = input("Do you wish to continue(y/n)?\n")
    if (res != 'y' and res != 'Y'):
        break


