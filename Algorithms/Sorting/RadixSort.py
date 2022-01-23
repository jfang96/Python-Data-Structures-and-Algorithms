from LinkedList import LinkedList

def radixSort(arr):
    buckets = []
    for i in range(0, 19):
        buckets.append(LinkedList())

    k = mostDigits(arr)
    # Iterate through digits
    for pos in range(0, k):
        # Iterate through array
        for i in range(0, len(arr)):
            digit = findDigit(arr[i], pos) # Find digit
            buckets[digit+9].add_last(arr[i]) # Add to queue
        idx = 0
        for bucket in buckets:
            while bucket.size > 0:
                arr[idx] = bucket.remove_first() # Remove from queue back to array
                idx += 1
        print(arr)

    return arr


def findDigit(myInt, pos):
    ''' Returns the pos'th digit of myInt '''
    strInt = str(abs(myInt)) # Get reversed string value
    if pos < len(strInt):
        return int(strInt[::-1][pos])
    else:
        return 0

def mostDigits(arr):
    ''' Returns the longest number of digits in arr '''
    # Get negative absolute value of the array
    tempArr = [-abs(ele) for ele in arr] 
    return len(str(min(tempArr))) - 1 # -1 to account for minus sign


arr = [17, 743, 672, 780, 917, 743, 623, 288, 432, 281, 76]
print(radixSort(arr))