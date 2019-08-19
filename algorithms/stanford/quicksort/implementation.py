# implementation of quicksort with 3 different partition methods

def loadInput(file):
    '''
    Input: file path, Output: array of integers
    '''
    with open(file, 'r') as f:
        array = [int(i) for i in f]
    return array


input = loadInput('inversiondata.txt')
print(len(input))
