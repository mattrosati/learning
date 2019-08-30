# implementation of quicksort with 3 different pivot choice methods
import sys

# fetching filepath
try:
    FILEPATH = sys.argv[1]
    if len(sys.argv) != 2:
        raise
except:
    print("Please provide only a path to file with array as the argument.")
    print("Example: quicksort.py <filepath>")
    sys.exit()

def loadInput(file):
    '''
    Input: file path, Output: array of integers
    '''
    with open(file, 'r') as f:
        array = [int(i) for i in f]
    return array

# initialize comparison counter, define a method counter for the three choice methods.
METHOD = 0
comp = 0

def quicksort(unsorted, left, right):
    '''
    input: unsorted array, left and right boundaries between which to sort.

    notice: left will always be the index of the first element of the subarray,
    while right will always be the index of the last array + 1.
    Sorts array in place by quicksort (and 3 different methods)

    output: none.
    '''
    length = right - left + 1
    # if array is one element or less, do nothing
    if length <= 1:
        return

    else:
        # update comp globally, choose pivot, and determine future position of pivot (which is its value)
        global comp
        comp += length - 1
        pivot = choosePivot(unsorted, left, right)
        pivot_value = unsorted[pivot] - 1

        # put pivot at beginning of subarray and partition
        unsorted[left], unsorted[pivot] = unsorted[pivot], unsorted[left]
        partition(unsorted, left, right)

        # recurse on split arrays
        quicksort(unsorted, left, pivot_value - 1)
        quicksort(unsorted, pivot_value + 1, right)
        return

def choosePivot(array, left, right):
    '''
    given array and left and right boundaries, returns an index of pivot
    chosen according to different methods.
    '''
    global METHOD
    if METHOD == 0:
        # always choose first element as pivot
        return left
    elif METHOD == 1:
        # always choose last element as pivot
        return right
    elif METHOD == 2:
        # choose median of first, last and middle element as pivot
        middle_index = (right + left)//2
        first = array[left]
        second = array[right]
        third = array[middle_index]
        if first < second:
            if third < first:
                return left
            elif third > second:
                return right
        else: # second < first
            if third < second:
                return right
            elif third > first:
                return left
        return middle_index


def partition(pivot_array, left, right):
    '''
    given array with pivot in left position, partitions array, no return value
    '''
    pivot = pivot_array[left]
    i = left + 1
    for j in range(i, right + 1):
        if pivot_array[j] < pivot:
            pivot_array[i], pivot_array[j] = pivot_array[j], pivot_array[i]
            i += 1
    pivot_array[i - 1], pivot_array[left] = pivot_array[left], pivot_array[i - 1]
    return

#run all three methods at once
while METHOD != 3:
    input = loadInput(FILEPATH)
    initial_right = len(input) - 1
    unsorted = input
    quicksort(unsorted, 0, initial_right)
    print("Number of comparisons for method", METHOD, "is:", comp)
    comp = 0
    METHOD += 1
