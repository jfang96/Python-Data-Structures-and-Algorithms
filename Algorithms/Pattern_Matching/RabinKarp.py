def RabinKarp(pattern, text):
    m = len(pattern)
    n = len(text)
    base = 2

    hash = calcHash(pattern, base) # Calculate initial hash
    print(hash)

    oldChar = "L"
    newChar = "Q"
    hash = updateHash(hash, oldChar, newChar, base)
    print(hash)

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
pattern = "Linked"
text = ""
print(RabinKarp(pattern, text))