def find_string_anagram(str, pattern):
    if len(pattern) > len(str): return []
    pattern_map = {}
    window_map = {}
    result = []
    for i in range(len(pattern)):
        if pattern[i] not in pattern_map:
            pattern_map[pattern[i]] = 0
        if str[i] not in window_map:
            window_map[str[i]] = 0
        pattern_map[pattern[i]] += 1
        window_map[str[i]] += 1
    if check_for_anagram(window_map, pattern_map):
        result.append(0)
    l = 0
    window_map[str[l]] -= 1
    if window_map[str[l]] <= 0:
        del window_map[str[l]]
    l +=1
    for r in range(len(pattern), len(str)):
        if str[r] not in window_map:
            window_map[str[r]] = 0
        window_map[str[r]] += 1
        if check_for_anagram(window_map, pattern_map):
            result.append(l)
        window_map[str[l]] -= 1
        if window_map[str[l]] <= 0:
            del window_map[str[l]]
        l += 1
    return result


def check_for_anagram(window_map, pattern_map):
    for i in window_map:
        if i not in pattern_map or window_map[i] != pattern_map[i]:
            return False
    return True


if __name__ == '__main__':
    print(find_string_anagram("abbcabc","abc"))
    print(find_string_anagram("ppqp","pq"))