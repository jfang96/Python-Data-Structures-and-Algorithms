def KMP(text, pattern):
    res = []

    ft = failureTable(pattern)

    def compare(char1, char2):
        compare.counter += 1
        return char1 == char2
    compare.counter = 0

    j, k = 0, 0 # j: Pattern index, k: Text index
    m, n = len(pattern), len(text) # m: Pattern length, n: Text length

    while k < n:
        if compare(pattern[j], text[k]):
            if j == m - 1:
                res.append(k - j) # Full match has been found
                k += 1
            else: # Case 1: Char matches
                j += 1
                k += 1
        elif j == 0: # Case 2: Mismatch, j = 0
            k += 1
        else: # Case 3: Mismatch, j != 0
            j = ft[j-1]
    
    return (res, compare.counter)


def failureTable(pattern):
    ft = [0] * len(pattern)
    iPrefix, iQuery = 0, 1 # Create indices
    while iQuery < len(pattern):
        # Match is found, increment indices
        if pattern[iPrefix] == pattern[iQuery]:
            ft[iQuery] = iPrefix + 1
            iPrefix += 1
            iQuery += 1
        # Match not found, failure table = 0 at index
        elif iPrefix == 0:
            ft[iQuery] = 0
            iQuery += 1
        # Match not found, prefix index > 1
        else:
            iPrefix = ft[iPrefix-1]
    
    return ft


pattern = "aaabb"
text = "aaaabbaab"
print(KMP(text, pattern))