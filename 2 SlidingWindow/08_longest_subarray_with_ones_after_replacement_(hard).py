def length_of_longest_substring(arr, k):
    ones = 0
    longest = 0
    window_start = 0
    for window_end in range(len(arr)):
        ones += arr[window_end]

        if window_end - window_start + 1 - ones > k:
            ones -= arr[window_start]
            window_start += 1
        longest = max(longest, window_end - window_start + 1)

    return longest


if __name__ == '__main__':
    print('longest contiguous subarray having all 1s', length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print('longest contiguous subarray having all 1s',length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
