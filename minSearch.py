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
        steps = 0
        for i in self.userList:
            steps += 1
            if i < minimum:
                minimum = i
        return minimum,steps

    def slowSearch(self):
        minimum = self.userList[0]
        steps = 0
        for i in self.userList:
            isMin = True
            for j in self.userList:
                steps += 1
                if j < i :
                    isMin = False

            if isMin:
                minimum = i
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
