# Implementing Heap and Quick Sort

import ctypes # to build the array
import random # to fill the array with random items
import string # for characters

def _make_new_array(_num_elem):
    """ Create a new ctypes array with cacapicty of _num_elem """
    return (_num_elem * ctypes.py_object)() # returns a ctypes array with _num_elem capacity

def _fill_array(_array, _num_elements):
    """ Fill _empty array with some random characters (lower/upper case)"""
    for i in range(_num_elements): # fill the arary with _num_elements
        _array[i] = random.choice(string.ascii_letters)
    return _array



def _heapify(_array_in, _num_elem, i): # heapify from leaf at i
    _greater_number = i      
    _left_child = 2 * i + 1  # position of _left_child from i
    _right_child = 2 * i + 2 # position of _right_child from i

    # don't need parent for this implementation > handled with children math
    _parent = (i - 1)//2     # position parent for either leaf (integer division handles odd #s)

    # check if left child exists and is greater than parent
    if _left_child < _num_elem and _array_in[i] > _array_in[_left_child]: # updated
        _greater_number = _left_child

    # check if right child exists and is greater than parent
    if _right_child < _num_elem and _array_in[_greater_number] > _array_in[_right_child]: # updated
        _greater_number = _right_child

    if _greater_number != i: # update root
        temp = _array_in[_greater_number]
        _array_in[_greater_number] = _array_in[i]
        _array_in[i] = temp

        # recur
        _heapify(_array_in, _num_elem, _greater_number)


def _heap_sort(_array_in): # main sort function
    _num_elem = len(_array_in)

    # build the heap
    for i in range(_num_elem // 2 - 1, -1, -1):
        _heapify(_array_in, _num_elem, i)

    # extract elements
    for i in range(_num_elem-1,0,-1): # starting from the bottom (or end)
        temp = _array_in[0]
        _array_in[0] = _array_in[i]
        _array_in[i] = temp

        _heapify(_array_in,i,0) # turn complete binary tree back into a heap


""" Quick sort code"""

def inplace_quick_sort(array_in,a,b):
    """Sort the list from array_in[a] to array_in[b] inclusive using quick-sort algorithim"""
    if a >= b: return       # already sorted
    pivot = array_in[b]     # set the pivot to the index b
    left = a                # scan rightward
    right = b - 1           # scan leftward

    while left <= right: # scan until markers meet or pass
        # scan until reaching value equal or larger than pivot or right marker
        while left <= right and array_in[left] > pivot:    # reversed here fixed ascend descend
            left += 1
            #right -= 1      # didn't work to reverse asecend / descend
        # scan until reaching value equal or smaller than pivot or left marker

        while left <= right and pivot > array_in[right]:   # reversed here fixed ascend descend
            right -= 1
            #left += 1       # didn't work to reverse asecend / descend

        if left <= right:
            array_in[left], array_in[right] = array_in[right], array_in[left]
            left, right = left + 1, right - 1
    # put pivot in it's final place (currently marked by left index)
    array_in[left], array_in[b] = array_in[b], array_in[left]

    # recur
    inplace_quick_sort(array_in, a, left - 1)
    inplace_quick_sort(array_in, left + 1, b)

if __name__ == "__main__":

    # create and fill an array with characters
    _n = 10 # number of elements in array

    # Heap sort
    _original_list = _make_new_array(_n) # create a new array with _n capacity
    array_in = _fill_array(_original_list, _n) # the _original_list filled with random characters

    # Quick sort
    _original_list2 = _make_new_array(_n)  # create a new array with _n capacity
    array_in2 = _fill_array(_original_list2, _n)  # the _original_list filled with random characters

    print("\nWeek 4, Lab 3: Heap Sort Demo")
    print("Unsorted array: ", end = "")
    print(*array_in) # print the elements of the original array")"""
    print("Sorted array: ", end = "")
    _heap_sort(array_in)
    print(*array_in)

    print("\nWeek 4, Lab 3: Quick-Sort Demo")
    print("Unsorted array: ", end="")
    print(*array_in2)  # print the elements of the original array")"""
    print("Sorted array: ", end="")
    inplace_quick_sort(array_in2,0, _n - 1)
    print(*array_in2)