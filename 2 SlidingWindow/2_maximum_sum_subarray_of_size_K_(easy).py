def max_sub_array_size_of_K(K, arr):
    max_subarray = 0
    window_start = 0
    window_sum = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end - window_start >= K-1:
            max_subarray = max(max_subarray, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_subarray


if __name__ == '__main__':
    print('Subarray [2, 1, 5, 1, 3, 2] maximum sum is ' + str(max_sub_array_size_of_K(3,[2, 1, 5, 1, 3, 2])))


