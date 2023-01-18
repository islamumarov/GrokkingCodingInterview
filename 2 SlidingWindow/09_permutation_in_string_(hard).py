def find_permutation(s2, s1):
    if len(s1) > len(s2):
        return False
    s1map = [0] * 26
    s2map = [0] * 26
    matches = 0
    for i in range(len(s1)):
        s1map[ord(s1[i]) - ord('a')] += 1
        s2map[ord(s2[i]) - ord('a')] += 1
    for i in range(26):
        matches += (1 if s1map[i] == s2map[i] else 0)
    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True
        index = ord(s2[r]) - ord('a')
        s2map[index] += 1
        if s2map[index] == s1map[index]:
            matches += 1
        elif s2map[index] == s1map[index] + 1:
            matches -= 1
        index = ord(s2[l]) - ord('a')
        s2map[index] -= 1
        if s2map[index] == s1map[index]:
            matches += 1
        if s2map[index] == s1map[index] - 1:
            matches -= 1
        l += 1
    return matches == 26


if __name__ == '__main__':
    print(find_permutation('oidbcaf', 'abc'))
    print(find_permutation("bcdxabcdy", "bcdxabcdy"))
    print(find_permutation("aaacb", "abc"))
