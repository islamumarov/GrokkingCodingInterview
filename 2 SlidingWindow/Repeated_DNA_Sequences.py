def find_repeated_sequences(s, k):
    if len(s) <= k:
        return []
    patterns = {}
    window_start = 0
    result = set()
    window_str = s[0:k]
    patterns[window_str] = 1
    for r in range(k, len(s)):
        window_str += s[r]
        window_start += 1
        window_str = s[window_start:window_start+k]
        if window_str in patterns:
            result.add(window_str)
        else:
            patterns[window_str] = 1

    return result



if __name__ == '__main__':
    print(str(find_repeated_sequences('GGGGGGGGGGGGGGGGGGGGGGGGG', 9)))
    print(str(find_repeated_sequences('AGCTGAAAGCTTAGCTG', 5)))