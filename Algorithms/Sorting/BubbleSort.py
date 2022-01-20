import timeit

def bubbleSort(arr):
    stopIndex = len(arr) - 1
    while stopIndex != 0:
        for i in range(stopIndex):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        stopIndex -= 1
    return arr

def bubbleSortOptimize1(arr):
    ''' Optimized to stop searching when no swaps are made'''
    stopIndex = len(arr) - 1
    swapMade = True
    while stopIndex != 0 and swapMade:
        for i in range(stopIndex):
            swapMade = False
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapMade = True
        stopIndex -= 1
    return arr

def bubbleSortOptimize2(arr):
    ''' Optimized to track last time a swap was made'''
    stopIndex = len(arr) - 1
    lastSwapped = 0
    while stopIndex != 0:
        for i in range(stopIndex):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                lastSwapped = i
        stopIndex = lastSwapped
    return arr


iterations = 10
arr = [5, 3, 7, 8, 6, 9, 1, 4, 2]
# arr = list(range(1000))[::-1]
# arr = list(range(1000))

start = timeit.default_timer()
for i in range(iterations): 
    bubbleSort(arr)
stop = timeit.default_timer()
print(f"Execution time is: {(stop - start)*1000} ms")

start = timeit.default_timer()
for i in range(iterations): 
    bubbleSortOptimize1(arr)
stop = timeit.default_timer()
print(f"Execution time is: {(stop - start)*1000} ms")

start = timeit.default_timer()
for i in range(iterations): 
    bubbleSortOptimize2(arr)
stop = timeit.default_timer()
print(f"Execution time is: {(stop - start)*1000} ms")
