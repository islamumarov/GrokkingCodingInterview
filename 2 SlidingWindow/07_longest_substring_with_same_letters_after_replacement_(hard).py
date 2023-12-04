def length_of_longest_substring(s, k):
    count = {}
    res = 0
    left = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)

        while (r - left + 1) - max(count.values()) > k:
            count[s[left]] -= 1
            left += 1
        res = max(res, r - left + 1)
    return res


if __name__ == '__main__':
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde",1))