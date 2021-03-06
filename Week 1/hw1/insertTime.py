import time
import random

"""
    Return an array of sorted integers using an insertion sort algorithm

    Keyword Arguments:
    array -- the unsorted array
"""
def insertsort(array):

    i = 0
    length = len(array)

    while(i < length):
        temp = array[i]
        j = i
        while(j > 0 and temp < array[j - 1]):
            array[j] = array[j - 1]
            j -= 1

        array[j] = temp
        i += 1

    return array

# Ranges to be used in the random array
n = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

# Run Merge Sort and collect the running time on the program
idx = 0
while (idx < len(n)):
    start = time.time()
    insertsort([random.random() for _ in range(n[idx])])
    end = time.time()
    runtime = (end - start)
    print("N: " + str(idx + 1), "Time: " + str(runtime))
    idx += 1