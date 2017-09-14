__author__ = 'sarvps'

'''Author: Sarv Parteek Singh
   Course: CISC 610
   Term: Late Summer
   HW: 6
   Problem: 3
   Brief:generates collision-free hash values for a given list of values
'''

def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])

    return sum%tablesize

alist = ['John','Ram','Sheila','Sneha','Sarv','Deep','Cathy','Sean','Mathew','Xu']
for i in alist:
    print("hash(%s) = %d",i,hash(i,11))