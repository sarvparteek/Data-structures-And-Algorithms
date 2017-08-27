__author__ = 'sarvps'

'''
    Author: Sarv Parteek Singh
    Course: CISC 610
    Term: Late Summer
    Brief: Check whether a string is palindrome using recursion
'''

def reverseString(str):
    if len(str) == 1:
        return str
    else:
        return str[-1] + reverseString(str[:-1])

def isPalindrome(str):
    return str == reverseString(str)

while(True):
    str = input("Enter the string you wish to check for being a palindrome\n")
    if (isPalindrome(str)):
        print("{} is a palindrome".format(str))
    else:
        print("{} is not a palindrome".format(str))
    choice = input("Do you wish to continue (y/n)?\n")
    if (choice != 'y' and choice != 'Y'):
        break

