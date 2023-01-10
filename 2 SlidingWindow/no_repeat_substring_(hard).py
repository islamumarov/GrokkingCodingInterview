def non_repeat_substring(str):
    window_start = 0
    longest_substring = 0
    substring = {}
    for window_end in range(len(str)):
        while str[window_end] in substring:
            substring[str[window_start]] -= 1
            if substring[str[window_start]] == 0:
                del substring[str[window_start]]
            window_start += 1
        substring[str[window_end]] = 1
        longest_substring = max(longest_substring, window_end - window_start + 1)
    return longest_substring


# More efficient approach
def non_repeat_substring_2(str):
    window_start = 0
    longest_substring = 0
    substring = {}
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in substring:
            window_start = max(window_start, substring[right_char] + 1)
        substring[right_char] = window_end
        longest_substring = max(longest_substring, window_end - window_start + 1)
    return longest_substring


if __name__ == '__main__':
    print(
        "The longest substring for aabccbb without any repeating characters is " + str(non_repeat_substring("aabccbb")))
    print("The longest substring for abbbb without any repeating characters is " + str(non_repeat_substring("abbbb")))
    print("The longest substring for abccde without any repeating characters is " + str(non_repeat_substring("abccde")))
    # second approach

    print("The longest substring for aabccbb without any repeating characters is " + str(non_repeat_substring_2("aabccbb")))
    print("The longest substring for abbbb without any repeating characters is " + str(non_repeat_substring_2("abbbb")))
    print("The longest substring for abccde without any repeating characters is " + str(non_repeat_substring_2("abccde")))
