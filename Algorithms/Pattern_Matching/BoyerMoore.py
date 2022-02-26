def BoyerMoore(text, pattern):
    last = BMLastTable(pattern)

    def compare(char1, char2):
        return char1 == char2

    res = []

    # Iterate through text
    i = 0
    while i <= len(text) - len(pattern): # Index for text
        j = len(pattern) - 1 # Index for pattern
        # Iterate backwards through pattern, comparing to text
        while j >= 0 and compare(text[i+j], pattern[j]):
            j -= 1
        if j == -1: # Pattern found
            res.append(i)
        else: # Text and pattern do not match
            shift = 0
            if text[i+j] in last: # Check if mismatched value exists in pattern
                shift = last[text[i+j]]
                if shift < j: 
                    i = i + j - shift # Shift to next matching value
                    continue
            else: # If doesn't exist in pattern, shift past value
                i = i + j
        i += 1
    return res

def BMLastTable(pattern):
    ''' Create dictionary of values : last_index for pattern '''
    last = {}
    for i in range(0, len(pattern)):
        last[pattern[i]] =  i
    return last




pattern = "ab"
text = "aaabaab"
print(BoyerMoore(text, pattern))