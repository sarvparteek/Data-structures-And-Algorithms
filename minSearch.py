__author__ = 'sarvps'

'''
    Author: Sarv Parteek Singh
    Course: CISC 610
    Term: Late Summer
    Data Structures & Algorithms by Miller
    Practice problem, Section 2.3
'''

class listManipulator():
    def __init__(self, ulist):
        self.userList = ulist

    def fastSearch(self):
        minimum = self.userList[0]
        steps = 1 # for minimum assignment
        for i in self.userList:
            steps += 1 # for if conditional
            if i < minimum:
                minimum = i
                steps += 1 #for minimum assignment
        return minimum,steps

    def slowSearch(self):
        minimum = self.userList[0]
        steps = 1 # for minimum assignment
        for i in self.userList:
            isMin = True
            steps += 1 # for isMin assignment
            for j in self.userList:
                steps += 1 #for if conditional
                if j < i :
                    isMin = False
                    steps += 1 # for isMin assignment

            steps += 1 #for if conditional
            if isMin:
                minimum = i
                steps += 1 #for minimum assignment
        return minimum,steps

    def getSize(self):
        return len(self.userList)

def main():

    ulist = [2, 30, 30, 4, 0, 50, -2, -24, -25]
    l = listManipulator(ulist)
    res = l.fastSearch()
    print("Fast search - List size: %d, Steps taken: %d, Minimum: %d " %(l.getSize(),res[1], res[0]))
    res = l.slowSearch()
    print("Slow search - List size: %d, Steps taken: %d, Minimum: %d " % (l.getSize(), res[1], res[0]))


main()
