def RabinKarp(pattern, text):
    m = len(pattern)
    n = len(text)

    hash = calcHash(pattern, 2) # Calculate initial hash with base = 2
    print(hash)

def calcHash(pattern, base):
    ''' Calculate hash of pattern with base. Assume hash function is ASCII. '''
    hash = 0
    m = len(pattern)
    for i, char in enumerate(pattern):
        hash += ord(char) * base**(m-(i+1))
    return hash


# Testing
pattern = "KnuthM"
text = ""
print(RabinKarp(pattern, text))