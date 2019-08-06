# algorithm to detect number of inversions in an array,
# also sorts array


def loadInput(file):
    '''
    Input: file path, Output: array of integers
    '''
    with open(file, 'r') as f:
        array = [int(i) for i in f]
    return array


input = loadInput('inversiondata.txt')
print(len(input))

def sortAndInversions(array):
    '''
    Consumes unsorted array and returns array of number of inversions and sorted array.
    Recursive, base case is one element array, or empty array
    '''
    length = len(array)
    #base case
    if length <= 1:
        return [array, 0]

    #recursive case (2 calls)
    middle = length//2
    x = sortAndInversions(array[0:middle])
    y = sortAndInversions(array[middle:])
    z = merge(x[0], y[0], x[1] + y[1])

    return z

def merge(before, after, acc):
    '''
    Inputs: two sorted arrays and accumulator of number of inversions.
    Returns an array of the sorted combined array, and updated number of split inversions.
    Split inversions is defined as number of pairs of entries (i, j)
    where i is an element of before and j is an element of after and i > j.
    Modified helper of marge sort.
    '''
    result = []
    i, j = 0, 0
    length1 = len(before)
    length2 = len(after)
    #make comparisons item-wise
    while i < length1 and j < length2:
        if before[i] <= after[j]:
            result.append(before[i])
            i += 1
        else:
            result.append(after[j])
            acc = acc + (length1 - i)
            j += 1

    #append rest of remaining array if one is shorter
    while i < length1:
        result.append(before[i])
        i += 1
    while j < length2:
        result.append(after[j])
        j += 1

    return [result, acc]

#code to return just number of inversions, sorted array for tests with len < 10
output = sortAndInversions(input)
if len(input) < 10:
    print("Sorted array:", output[0])
print("Number of inversions is ", str(output[1]))
