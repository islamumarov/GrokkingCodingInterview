def longest_substring_with_k_distinct(str, k):
    longest = -1
    dict = {}
    window_start = 0
    for j, i in enumerate(str):
        if i in dict:
            dict[i] +=1
        else:
            dict[i] = 1
        while(len(dict) > k):
            dict[str[window_start]] -= 1
            if dict[str[window_start]] == 0:
                del dict[str[window_start]]
            window_start += 1
        longest = max(longest, j - window_start + 1)
    return longest


if __name__ == '__main__':
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))