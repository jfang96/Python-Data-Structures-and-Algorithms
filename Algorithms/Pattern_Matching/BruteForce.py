def bruteForce(text, pattern):
    '''Algorithm BruteForce(text, pattern)
	for t <- 0 to n - m
		i <- 0
		while i <= m - 1
			if pattern[i] matches text[i + t]
				if i < m - 1
					continue the inner loop
				else
					return index of match in text
			else
                stop the inner loop''' 
    
    n = len(text)
    m = len(pattern)
    # Iterate through the text
    for t in range(0, n-m+1): 
        i = 0 
        # Iterate through pattern
        while i <= m-1:
            print(f"index: {i}, pattern: {pattern[i]}, text: {text[i+t]}")
            # If chars match, continue until end of the pattern
            if pattern[i] == text[i+t]:   
                i += 1
                if i > m-1:
                    return i+t-m
            # If chars don't match, move to next char in text
            else:
                break


text = "ababcabbabb"
pattern = "babb"

print(bruteForce(text, pattern))