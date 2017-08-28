__author__ = 'sarvps'

'''
    Author: Sarv Parteek Singh
    Course: CISC 610
    Term: Late Summer
    Mid-term exam, Problem 3
    Brief: Finds whether the sequence has more vowels than consonants
'''

def vowelVsConsonantCount(str):
    if len(str) == 1:
        return alphabetScore(str)
    else:
        return alphabetScore(str[0]) + vowelVsConsonantCount(str[1:])

def alphabetScore(c):
    if c in "aeiouAEIOU":
        return 1
    else:
        return -1

def hasMoreVowels(str):
    if vowelVsConsonantCount(str) > 0:
        return True
    else:
        return False

while True:
    s = input("Enter test string\n")
    print("The statement 'This string has more vowels than consonants is' ", hasMoreVowels(s))
    res = input("Do you wish to continue(y/n)?\n")
    if (res != 'y' and res != 'Y'):
        break