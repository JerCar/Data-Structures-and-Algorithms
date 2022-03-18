
import ctypes # to build the array
import random # to fill the array with random characters
import string # for random characters

""" Implemention of Insertion, Bubble and Selection Sort """


def _make_new_array(_num_elem):
    """ Create a new ctypes array with capacity of _num_elem """
    return (_num_elem * ctypes.py_object)() # returns a ctypes array with _num_elements capacity

def _fill_array(_array, _num_elements): # fill _emptry array with some random characters (lower/upper case)
    for i in range(_num_elements):    # fill the array with _n elements
        _array[i] = random.choice(string.ascii_letters)
    return _array

def _insertion_sort(_array_to_sort):
    """ Insertion sort _array_to_sort (characters) in descending order """
    for i in range(1, len(_array_to_sort)): # every element from ndx 1 to end of array
        k = i - 1 # set k equal to the index before i
        current_element = _array_to_sort[i] # set current_element to the value at the index of _array_to_sort

        while k >= 0 and _array_to_sort[k] < current_element:
            _array_to_sort[k + 1] = _array_to_sort[k]
            k -= 1

        _array_to_sort[k + 1] = current_element

    return _array_to_sort

def _bubble_sort(_array_to_sort):
    """ Bubble sort _array_to_sort (characters) in descending order """
    for passnum in range(len(_array_to_sort)-1,0,-1):
        for i in range(passnum):
            if _array_to_sort[i] < _array_to_sort[i+1]:
                temp = _array_to_sort[i]
                _array_to_sort[i] = _array_to_sort[i+1]
                _array_to_sort[i+1] = temp
    return _array_to_sort

def selectionSort(alist):
    """ Selection sort _array_to_sort (characters) in descending order """
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1,fillslot + 1):
            if alist[location] < alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

if __name__ == "__main__":

    # insertion sort boiler code
    _n = 17 # number of elements in array set to _n
    _original_list = _make_new_array(_n) # create a new array with _n capacity
    x = _fill_array(_original_list, _n) # the _original_list filled with random characters
    print("\nWeek 3, Lab 2: Insertion sort Demo")
    print("Unsorted array: ", end = "")
    print(*x) # print the elements of the original array

    _sorted_final_array = _insertion_sort(x)
    print("Sorted array: ", end = "")
    print(*_sorted_final_array)

    # bubble sort boiler code
    _n = 17  # number of elements in array set to _n
    _original_list2 = _make_new_array(_n)  # create a new array with _n capacity
    y = _fill_array(_original_list2, _n)  # the _original_list filled with random characters
    print("\nWeek 3, Lab 2: Bubble sort Demo")
    print("Unsorted array: ", end = "")
    print(*y) # print the elements of the original array

    _sorted_final_array2 = _bubble_sort(y)
    print("Sorted array: ", end="")
    print(*_sorted_final_array2)  # print the elements of the original array

    # insertion sort boiler code
    _n = 17  # number of elements in array set to _n
    _original_list3 = _make_new_array(_n)  # create a new array with _n capacity
    y = _fill_array(_original_list3, _n)  # the _original_list filled with random characters
    print("\nWeek 3, Lab 2: Selection Sort Demo")
    print("Unsorted array: ", end="")
    print(*y)  # print the elements of the original array

    _sorted_final_array3 = _bubble_sort(y)
    print("Sorted array: ", end="")
    print(*_sorted_final_array3)  # print the elements of the original array

