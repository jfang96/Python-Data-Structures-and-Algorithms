from lib2to3.pygram import pattern_symbols


def failureTable(pattern):
    ft = [0] * len(pattern)
    i, j = 0
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            ft[j] = i + 1
            i += 1
            j += 1
        elif pattern[i] != pattern[j] and i == 0:
            ft[j] = 0
            j += 1
        else:
            i = ft[i-1]
    
    return ft