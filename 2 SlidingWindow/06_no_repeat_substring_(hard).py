def non_repeat_substring(str):
    dict = {}
    max_len = 0
    window_start = 0
    for i, j in enumerate(str):
        while j in dict:
            del dict[str[window_start]]
            window_start += 1
        if j not in dict:
            dict[j] = 1
        max_len = max(max_len, len(dict))
    return max_len


if __name__ == '__main__':
    print(
        "The longest substring for aabccbb without any repeating characters is " + str(non_repeat_substring("aabccbb")))
    print("The longest substring for abbbb without any repeating characters is " + str(non_repeat_substring("abbbb")))
    print("The longest substring for abccde without any repeating characters is " + str(non_repeat_substring("abccde")))
    # second approach