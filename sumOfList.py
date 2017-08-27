__author__ = 'sarvps'

'''
    Author: Sarv Parteek Singh
    Course: CISC 610
    Term: Late Summer
'''

class summation():
    def __init__(self):
        pass

    def directSum(self, uList):
        sum = 0
        for i in uList:
            sum += i
        return sum

    def recursiveSum(self,uList):
        if len(uList) == 1:
            return uList[0]
        else:
            return uList[0] + self.recursiveSum(uList[1:])

def main():
    list1 = list(range(10))
    s = summation()
    print("Direct sum: ",s.directSum(list1))
    print("Recursive sum: ", s.recursiveSum(list1))

main()
