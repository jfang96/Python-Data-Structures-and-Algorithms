def contiguousSum_bruteforce(nums):
    localMax = 0
    globalMax = 0

    for i in range(0, len(nums)):
        localMax = nums[i]
        for j in range(i+1, len(nums)):
            localMax += nums[j]
            if globalMax < localMax:
                globalMax = localMax

    return globalMax

def contiguousSum_kadane(nums):
    localMax = 0
    globalMax = 0

    for i in range(0, len(nums)):
        localMax += nums[i]
        if globalMax < localMax:
            globalMax = localMax
        localMax = max(localMax, 0)

    return globalMax


def contiguousSum_dp(nums):
    localMax = [0]
    globalMax = [0]
    dp = []

    for i in range(0, len(nums)):
        localMax += nums[i]

nums = [-1, 2, -1, 4, -3, 1, 3]
print(contiguousSum_bruteforce(nums))