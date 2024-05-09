def lengthOfLongestSubstring(s: str) -> int:
    Window_start = 0
    freq = {}
    Max_len = -1
    for i in range(0, len(s)):
        while s[i] in freq:
            del freq[s[Window_start]]
            Window_start += 1
        freq[s[i]] = 1
        Max_len = max(Max_len, i - Window_start + 1)
    return Max_len


if __name__ == '__main__':
    print("Length of the longest substring: " + str(lengthOfLongestSubstring("abcabcbb")))
    print("Length of the longest substring: " + str(lengthOfLongestSubstring("bbbbb")))
