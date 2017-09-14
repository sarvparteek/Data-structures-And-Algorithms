__author__ = 'sarvps'

'''Author: Sarv Parteek Singh
   Course: CISC 610
   Term: Late Summer
   HW: 6
   Problem: 1
'''

import numpy as np
import pylab as pl
import timeit
import math

def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1

    return found

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found

b = -10;
rad = 5;
c = 2;
d1, d2 = b + rad, b - rad
print(d1, d2)

xr1 = -2*c / (d1 if abs(d1) > abs(d2) else d2)
xr2 = -2*c / (d2 if abs(d1) > abs(d2) else d1)
print(xr1, xr2)

d1, d2 = b + rad, b - rad
xr11 = -2*c / max(abs(d1), abs(d2))
xr21 = -2*c / min(abs(d1), abs(d2))
print(xr11, xr21)

test_ranges = range(100,10001,200)
seq_search_times = []
bin_search_times = []
log_list = []
scaling = 0.
print("#### List size, Sequential search time, Binary search time")
for i in test_ranges:
    seq_search_times = []
for i in test_ranges:
    t_seq = timeit.Timer("y = sequentialSearch(alist, alist[-1])",
                     "from __main__ import sequentialSearch,alist")
    t_bin = timeit.Timer("y = binarySearch(alist, alist[-1])",
                     "from __main__ import binarySearch,alist")
    alist = list(range(i))
    seq_time = t_seq.timeit(number = 1000)
    bin_time = t_bin.timeit(number = 1000)
    seq_search_times.append(seq_time)
    bin_search_times.append(bin_time)
    if i == test_ranges[0]:
        scaling = math.log(i,2)/bin_time
    log_list.append(math.log(i,2)/scaling)
    print("%d,%10.3f, %10.3f" % (i, seq_time, bin_time))

#Plot a comparison between sequential and binary search
pl.figure(1)
pl.plot(test_ranges, seq_search_times, 'r', label = 'Seq. search')
pl.plot(test_ranges, bin_search_times, 'b', label = 'Bin. search')
pl.plot(test_ranges, log_list, 'm', label = 'log n')
pl.xlabel('List size')
pl.ylabel('Operation time (ms)')
pl.title('Time complexity of sequential and binary search')
pl.grid(True)

#Plot to show that binary search is log n
pl.figure(2)
pl.plot(test_ranges, bin_search_times, 'b', label = 'Bin. search')
pl.plot(test_ranges, log_list, 'm', label = 'log n')
pl.xlabel('List size')
pl.ylabel('Operation time (ms)')
pl.title('Comparison of binary search and log n (scaled)')
pl.grid(True)

pl.show()