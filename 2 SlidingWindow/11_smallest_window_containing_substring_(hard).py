def find_substring(str, pattern):
    pattern_map = {}
    str_map = {}
    l = 0
    for i in pattern:
        pattern_map[i] = 1 + pattern_map.get(i,0)
    have, need = 0, len(pattern_map)
    res, resLen = [-1,-1], float("infinity")
    for r in range(len(str)):
        c = str[r]
        str_map[c] = 1 + str_map.get(c, 0)
        if c in pattern_map and str_map[c] == pattern_map[c]:
            have += 1
        while have == need:
            if (r-l+1) < resLen:
                res = [l, r]
                resLen = r-l+1
            str_map[str[l]] -= 1
            if str[l] in pattern_map and str_map[str[l]] < pattern_map[str[l]]:
                have -= 1
            l += 1
    l,r = res
    return str[l:r+1] if resLen != float("infinity") else ""


if __name__ == '__main__':
    print(find_substring("aa", "aa"))
    print(find_substring("ADOBECODEBANC", "ABC"))
