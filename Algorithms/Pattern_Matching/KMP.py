def KMP(pattern, text):
    ft = failureTable(pattern)

    j, k = 0, 0
    m, n = len(pattern), len(text)

    while k < n:
        if pattern[j] == text[k]:
            if j == m - 1:
                return k # Full match has been found
            else: # Case 1: Char matches
                j += 1
                k += 1
        elif pattern[j] != text[k] and j == 0: # Case 2: Mismatch, j = 0
            k += 1
        else: # Case 3: Mismatch, j != 0
            j = ft[j-1]


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
        elif pattern[iPrefix] != pattern[iQuery] and iPrefix == 0:
            ft[iQuery] = 0
            iQuery += 1
        # Match not found, prefix index > 1
        else:
            iPrefix = ft[iPrefix-1]
    
    return ft