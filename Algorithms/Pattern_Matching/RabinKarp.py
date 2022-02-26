def RabinKarp(pattern, text):
    ''' Rabin-Karp Pattern-matching algorithm 
        Time: O(mn)
        Space: O(1); pattern and text hashes, results arr    
    '''
    res = []

    m = len(pattern)
    n = len(text)
    base = 2

    hash = calcHash(pattern, base) # Calculate initial pattern hash
    textHash = calcHash(text[:m], base) # Calculate hash of first length-m substring in text

    i = 0
    while i <= n - m: # Iterate through text
        if hash == textHash: # Hashes match! Now compare char by char
            iText = i
            iPattern = 0
            while text[iText] == pattern[iPattern]: # Compare char by char
                if iPattern == m - 1: # Complete match found
                    res.append(i) 
                    break
                iText += 1
                iPattern += 1
        if i < m - n: # Check if at end of text
            textHash = updateHash(textHash, text[i], text[i+m], base) # Update text hash with next char
        i += 1 

    return res

def calcHash(pattern, base):
    ''' Calculate hash of pattern with base. Assume hash function is ASCII. '''
    hash = 0
    m = len(pattern)
    for i, char in enumerate(pattern):
        hash += ord(char) * base**(m-(i+1))
    return hash

def updateHash(oldHash, oldChar, newChar, base):
    ''' Update current hash by removing oldChar from hash and adding newChar. '''
    m = len(pattern)
    return (oldHash - ord(oldChar) * base**(m-1)) * base + ord(newChar)
    

# Testing
pattern = "aaab"
text = "aaabaaab"
print(RabinKarp(pattern, text))