"""
DISCLAIMER:
The source code contained in this file was written haphazardly in a short
amount of time during a live presentation setting. It should not be taken
as an exemplar of good design and organization of program source code!
The main purpose of the exercise was to demonstrate rapidly how the steps
of an algorithm may be transformed into Python statements.

We do not warrant against bad habits developed from studying this code.
USE AT YOUR OWN RISK!


Crude implementation of a selection sort algorithm.
See Program 4.2.4 in the text for a more concise and cleaner implementation
of a similar sorting algorithm, insertion sort.
"""

import random

def find_index_of_minimum(a, start, stop):
    min_index = start
    min_value = a[start]
    for index in range(start, stop):
        if a[index] < min_value:
            min_value = a[index]
            min_index = index
    return min_index

def exchange_elements(a, index1, index2):
    """
    given two indices into array a, exchange their values
    """
    temp = a[index1]
    a[index1] = a[index2]
    a[index2] = temp

def sort_my_array(a):
    # for each element in my unsorted array
    num_elements = len(a)
    for current_index in range(num_elements):
        # find the index of the minimum in the subarray
        # between my current index and the end
        index_of_min = find_index_of_minimum(a, current_index, num_elements)
        # exchange my current element with the minimum element
        exchange_elements(a, current_index, index_of_min)


a = []
for i in range(10):
    a += [random.randrange(1, 100)]

print(a)
sort_my_array(a)
print(a)
