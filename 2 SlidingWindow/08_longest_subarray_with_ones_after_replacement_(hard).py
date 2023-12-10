
#Given an array containing 0s and 1s,
# if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.
def length_of_longest_substring(nums, k):
    window_start, count_of_ones_in_window, total_max = 0, 0, 0
    for i, j in enumerate(nums):
        if j == 1:
            count_of_ones_in_window += 1

        if (i - window_start - count_of_ones_in_window + 1) > k:
            if nums[window_start] == 1:
                count_of_ones_in_window -= 1
            window_start += 1

        total_max = max(i - window_start + 1, total_max)
    return total_max


if __name__ == '__main__':
    print('longest contiguous subarray having all 1s ', length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print('longest contiguous subarray having all 1s ',length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
