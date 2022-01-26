def bruteForce(text, pattern):    
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
                    return i+j-m
            # If chars don't match, move to next char in text
            else:
                break


text = "ababcabbabbds"
pattern = "babb"

print(bruteForce(text, pattern))