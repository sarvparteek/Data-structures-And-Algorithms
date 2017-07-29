__author__ = 'sarvps'

'''Author: Sarv Parteek Singh
   Course: CISC 610
   Term: Late Summer
   HW: 2
   Problem: 2, part 4
   Note: The code assumes that the elements in the array are distinct
   References:
    1) Lecture notes from MIT OCW 6.006, Fall 2011, Lec-4
    2) http://www.geeksforgeeks.org/heap-sort/
'''

# ------------------ Part 4 -------------------------------------------
    #Methods to visualize a list as a binary tree
def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def parent(i):
    return (i-1)//2


def max_heapify(A, i, size):
    l = left(i)
    r = right(i)
    largest = i

    #If the left child exists and is greater than the root of this sub-tree
    if (l < size and A[l] > A[i]):
        largest = l

    # If the right child exists and is greater than the root of this sub-tree
    if (r < size and A[r] > A[largest]):
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i] # exchange the largest number with the value at i
        max_heapify(A, largest, size) #max-heapify the root

def build_max_heap(A):
    for i in range(len(A)//2, -1, -1): # Start from n/2 because n/2+1 onwards are all leaves of the tree
        max_heapify(A, i, len(A))

def heapSort(A):
    build_max_heap(A)

    #Extract elements one-by-one
    n = len(A)
    for i in range(n-1,0,-1):
        A[i],A[0] = A[0],A[i] # Swap the root of tree with the last element
        max_heapify(A, 0, i)

    return A

def searchSmallest(A,k):
    B = heapSort(A)
    return B[k-1] #kth smallest number

'''
#Test code
arr = [23, 34, 54, 64, 65, 57]
C = searchSmallest(arr,3)
print(C)
'''





