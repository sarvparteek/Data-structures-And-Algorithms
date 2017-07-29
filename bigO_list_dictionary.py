__author__ = 'sarvps'

'''Author: Sarv Parteek Singh
   Course: CISC 610
   Term: Late Summer
   HW: 2
   Problem: 2, parts 1,2 & 3
'''

import numpy as np
import pylab as pl
import timeit
import random

# ------------------------- Part 1 --------------------------------------
test_ranges = range(10000,1000001,20000)
list_times = []
print('############# Indexing from a list ################')
for i in test_ranges:
    t = timeit.Timer("y = x[random.randrange(%d)]" % i, #access a random index
                     "from __main__ import random,x")
    x = list(range(i))
    list_time = t.timeit(number = 1000)
    list_times.append(list_time)
    print("%d,%10.3f" % (i,list_time))

#Plot results for part 1
pl.figure(1)
pl.plot(test_ranges, list_times)
pl.xlabel('List size')
pl.ylabel('Operation time (ms)')
pl.title('Time complexity of indexing operation on a list')
pl.ylim([0,0.05]) # Uncommenting this will clearly show that the operation is O(1). Otherwise, we just see noise
pl.grid(True)

#---------------Part 2 ----------------------------------------
dict_set_times = []
dict_get_times = []
print('########## Get vs set in a dictionary ##############')
print('Dictionary size, get time, set time')
for i in test_ranges:
    t_get = timeit.Timer("y = x.get(random.randrange(%d))" % i, #access a random index
                         "from __main__ import random,x")
    t_set = timeit.Timer("x[random.randrange(%d)] = 'Test'" % i,  # access a random index
                         "from __main__ import random,x")
    x = {j: None for j in range(i)}

    dict_get_time = t_get.timeit(number = 1000)
    dict_get_times.append(dict_get_time)
    dict_set_time = t_set.timeit(number=1000)
    dict_set_times.append(dict_set_time)

    print("%d,%10.3f,%10.3f" % (i,dict_get_time,dict_set_time))

#Plot results for part 2
pl.figure(2)
pl.plot(test_ranges, dict_get_times, 'r', label = 'Get')
pl.plot(test_ranges, dict_set_times, 'b', label = 'Set')
pl.legend(loc = 'upper left')
pl.xlabel('Dictionary size')
pl.ylabel('Operation time (ms)')
pl.title('Time complexity of get & set operations on a dictionary')
pl.ylim([0,0.05]) # Uncommenting this will clearly show that the operation is O(1). Otherwise, we just see noise
pl.grid(True)

# ---------------- Part 3 ---------------------------------
'''The approach used here differs from the previous cases. A random number between 0 and the last number in the list
or dictionary cannot be used for two reasons:
1) Every operation in timeit deletes an element. This means that in case of a list, if 500 elements have been deleted,
and an attempt is made to access/delete the (last-100)th element, an error would result since that element would be
out of bounds of the list.
2) Even if the above situation is taken care of by ensuring that the random numbers are generated from 
range(i.e. last element of list/dict) - # of repeat operations by timeit,
the problem would be solved only for a list. In case of a list, deleting an element re-structures the indices for
the list. That is, the number of indices are reduced by 1 per deletion. However, in case of a dictionary, there is no
such indexing mechanism. Thus, if a randomly generated list is used and any element is repeated, then on attempting to
delete that key, a key error would be generated. For instance, if 0 is generated as a random number during one iteration 
of timeit resulting in dictionary's key 0 being deleted, and thereafter, 0 is again generated as a random number during
a subsequent iteration, attempting to delete key 0 would result in a key error'''
dict_del_times = []
list_del_times = []

print('########## Del operation in list vs dictionary ##############')
print('Size, List time, Dictionary time')
for i in test_ranges:
    t_list = timeit.Timer("del l[next(list_iter)]", #delete a random member
                          "from __main__ import random,l,list_iter")
    t_dict = timeit.Timer("del d[next(dict_iter)]",  # delete a random member
                          "from __main__ import random,d,dict_iter")

    d = {j: None for j in range(i)}
    dict_iter = iter(random.sample(range(i-1000), 1000)) # Create a list of unique random numbers
    dict_del_time = t_dict.timeit(number=1000)
    dict_del_times.append(dict_del_time)

    l = list(range(i))
    list_iter = iter(random.sample(range(i-1000), 1000)) # Create a list of unique random numbers
    list_del_time = t_list.timeit(number=1000)
    list_del_times.append(list_del_time)

    print("%d,%10.3f,%10.3f" % (i,list_del_time,dict_del_time))

#Plot results for part 3
pl.figure(3)
pl.plot(test_ranges, list_del_times, 'r', label = 'List')
pl.plot(test_ranges, dict_del_times, 'b', label = 'Dictionary')
pl.legend(loc = 'upper left')
pl.xlabel('Size')
pl.ylabel('Operation time (ms)')
pl.title('Time complexity of del operation on a list & dictionary')
pl.grid(True)
pl.show()