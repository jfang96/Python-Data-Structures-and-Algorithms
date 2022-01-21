def cocktailSort(arr):
    swapsMade = True
    startInd = 0
    endInd = len(arr) - 1
    while swapsMade:
        swapsMade = False
        for i in range(startInd, endInd):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapsMade = True
                endInd = i
        if swapsMade: # Reverse direction
            swapsMade = False
            for i in reversed(range(startInd+1, endInd+1)):
                if arr[i-1] > arr[i]:
                    arr[i-1], arr[i] = arr[i], arr[i-1]
                    swapsMade = True
                    startInd = i
    return arr

arr = [5, 3, 6, 1, 9, 4, 2, 8, 7]
print(cocktailSort(arr))

