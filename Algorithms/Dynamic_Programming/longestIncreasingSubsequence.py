def lis1(arr) -> int:
    ''' Recursion method. LIS in [i-1, len] = longest LIS in [i, N] + 1
        Iterate through subproblems from back of array.
        Time: O(2^n)
        Space: O(n)'''

    def lis_recurse(curr):
        count = 1
        if curr == 0:
            return 1
        # Iterate backwards of the subarray
        for i in reversed(range(curr)):
            if arr[curr] > arr[i]:
                count = max(count, 1 + lis_recurse(arr, i))
        return count

    maxCount = 1
    for i in range(len(arr)):
        maxCount = max(maxCount, lis_recurse(arr, i))

    return maxCount


def lis2(arr) -> int:
    ''' Recursion method with memoization. 
        Time: O(n^2)
        Space: O(n) for storing helper array'''
    
    def lis_recurse(arr, curr):
        if curr in lisDict:
            return lisDict[curr]

        count = 1
        if curr == 0:
            return 1
        for i in reversed(range(curr)):
            if arr[curr] > arr[i]:
                count = max(count, 1 + lis_recurse(arr, i))

        lisDict[curr] = count
        return count

    
    maxCount = 1
    for i in range(0, len(arr)):
        lisDict = {} # create dict to hold previously calculated lis values
        maxCount = max(maxCount, lis_recurse(arr, i))

    return maxCount

def lis3(arr):
    ''' Dynamic Programming, naive.
        Time: O(n^2)
        Space: O(n) for storing helper array'''

    lisArr = [1] * len(arr) # Helper array to store prev results

    for i in range(len(arr)):
        for j in range(0, i):
            if arr[j] < arr[i]:
                lisArr[i] = max(lisArr[i], lisArr[j] + 1)
    
    return max(lisArr)



arr = [10, 22, 9, 33, 21, 50, 41, 60]
arr = [1, 7, 3, 5, 2, 8, 10, 24, 3, 4]
print(lis2(arr))