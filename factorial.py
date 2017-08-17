__author__ = 'sarvps'

'''
    Author: Sarv Parteek Singh
    Course: CISC 610
    Term: Late Summer
    HW: 3
    Problem: 1
'''

def fact(num):

    if num <= 1:
        return 1
    else:
        return num * fact(num-1)

def reverseList(inputList):
    if len(inputList) == 1:
        return [inputList[0]]
    else:
        return [inputList.pop()] + reverseList(inputList)

#Test for factorial
x = int(input("Enter the number\n"))
print("The factorial of %d is %d" %(x,fact(x)))

#Test for list reversal
y = list(range(10))
print("Reversed list is : ", reverseList(y))