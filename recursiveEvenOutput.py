__author__ = 'sarvps'

'''
    Author: Sarv Parteek Singh
    Course: CISC 610
    Term: Late Summer
    Final exam, Problem 2
    Brief: Print out positive even numbers between two given numbers using recursion
'''

def evenOutput(lower,upper):
    if upper - lower <= 1:
        if lower %2 == 0:
            print(lower)
        else:
            print(upper)
    else:
        if lower %2 == 0:
            if lower >0:
                print(lower)
            lower = lower + 2
        else:
            lower = lower + 1

        evenOutput(lower, upper)

evenOutput(-12,24)
