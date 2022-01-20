import timeit

def bubbleSort(arr):
    stopIndex = len(arr) - 1
    steps = 0
    while stopIndex != 0:
        for i in range(stopIndex):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            steps += 1
        stopIndex -= 1
    return arr, steps

def bubbleSortOptimize1(arr):
    ''' Optimized to stop searching when no swaps are made'''
    stopIndex = len(arr) - 1
    swapMade = True
    steps = 0
    while stopIndex != 0 and swapMade:
        swapMade = False
        for i in range(stopIndex):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapMade = True
            steps += 1
        stopIndex -= 1
    return arr, steps

def bubbleSortOptimize2(arr):
    ''' Optimized to track last time a swap was made'''
    stopIndex = len(arr) - 1
    steps = 0
    while stopIndex != 0:
        lastSwapped = 0
        for i in range(stopIndex):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                lastSwapped = i
            steps += 1
        stopIndex = lastSwapped
    return arr, steps


iterations = 1000
arr = [5, 3, 6, 1, 9, 4, 2, 8, 7]
# arr = list(range(1000))[::-1]
# arr = list(range(1000))

start = timeit.default_timer()
for i in range(iterations): 
    (temp, steps) = bubbleSort(list(arr))
stop = timeit.default_timer()
print(f"Execution time is: {(stop - start)*1000} ms over {steps} steps")

start = timeit.default_timer()
for i in range(iterations): 
    (temp, steps) = bubbleSortOptimize1(list(arr))
stop = timeit.default_timer()
print(f"Execution time is: {(stop - start)*1000} ms over {steps} steps")

start = timeit.default_timer()
for i in range(iterations): 
    (temp, steps) = bubbleSortOptimize2(list(arr))
stop = timeit.default_timer()
print(f"Execution time is: {(stop - start)*1000} ms over {steps} steps")