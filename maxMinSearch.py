__author__ = 'sarvps'

'''
    Author: Sarv Parteek Singh
    Course: CISC 610
    Term: Late Summer
    Mid-term exam, Problem 1, 4
    Brief: Finds maximum and minimum in the input sequence using recursion & then using less than 3n/2 steps
    References: http://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/
'''

def findOptima(uList):
    if len(uList) == 1:
        return uList[0],uList[0]
    else:
        return max(uList[0],findOptima(uList[1:])[0]),min(uList[0],findOptima(uList[1:])[1])

def fastFindOptima(uList):
    min = 0
    max = 0
    startInd = 0
    if (len(uList) %2 == 0):
        if(uList[0] > uList[1]):
            min = uList[1]
            max = uList[0]
        else:
            min = uList[0]
            max = uList[1]
        startInd = 2
    else:
        min = uList[0]
        max = uList[1]
        startInd = 1

    for i in range(startInd,len(uList)-1, 2):
        if uList[i] < uList[i+1]:
            if uList[i] < min:
                min = uList[i]
            if uList[i+1] > max:
                max = uList[i+1]
        else:
            if uList[i+1] < min:
                min = uList[i+1]
            if uList[i] > max:
                max = uList[i]

    return max,min

#Test
uList = list(range(15))
maxi,mini = findOptima(uList)
fmaxi,fmini = fastFindOptima(uList)
print("Sequence = {} | Max = {} | Min = {}".format(uList,maxi,mini))
print("Sequence = {} | Max = {} | Min = {}".format(uList,fmaxi,fmini))