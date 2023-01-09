def longest_substring_with_k_distinct(str, k):
    window_start = 0
    chars = {}
    max_len = 0
    for window_end in range(len(str)):
        if str[window_end] not in chars:
            chars[str[window_end]] = 0
        chars[str[window_end]] += 1
        while len(chars) > k:
            chars[str[window_start]] -= 1
            if chars[str[window_start]] == 0:
                del chars[str[window_start]]
            window_start += 1
        max_len = max(max_len, window_end - window_start + 1)
    return max_len


if __name__ == '__main__':
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))
