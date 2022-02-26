from lib2to3.pygram import pattern_symbols


def KMP(pattern, text):
    ft = failureTable(pattern)

def failureTable(pattern):
    ft = [0] * len(pattern)
    prefix, query = 0 # Create indices
    while query < len(pattern):
        # If match is found, 
        if pattern[prefix] == pattern[query]:
            ft[query] = prefix + 1
            prefix += 1
            query += 1
        elif pattern[prefix] != pattern[query] and prefix == 0:
            ft[query] = 0
            query += 1
        else:
            prefix = ft[prefix-1]
    
    return ft