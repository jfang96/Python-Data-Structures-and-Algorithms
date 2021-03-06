def bruteForce(text, pattern): 
    ''' Brute force pattern matching algorithm
        Time: O(mn)
        Space: O(1); results arr
    '''   
    res = []

    n = len(text)
    m = len(pattern)
    # Iterate through the text
    for i in range(0, n-m+1): # Index for text
        j = 0 # Index for pattern
        # Iterate through pattern
        while j <= m-1:
            # print(f"index: {i}, pattern: {pattern[i]}, text: {text[i+t]}")
            # If chars match, continue to next char
            if pattern[j] == text[i+j]:   
                j += 1
                if j > m-1: # All chars match! Return the index where pattern starts
                    res.append(i+j-m)
                    break
            # If chars don't match, move to next char in text
            else:
                break
    
    return res

# Testing
text = "ababbcabbabbds"
pattern = "babb"

print(bruteForce(text, pattern))