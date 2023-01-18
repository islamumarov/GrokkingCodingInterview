def smallest_subarray_with_given_sum(s, arr):
    window_start = 0
    window_sum = 0
    window_min = len(arr) + 1
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            window_min = min(window_min, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    if window_min >= len(arr) + 1:
        return 0
    else:
        return window_min


if __name__ == '__main__':
    print('Smallest sub arrays with a sum greater than or equal to 7 Is \n ' + str(
        smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print('Smallest sub arrays with a sum greater than or equal to 8 Is \n ' + str(
        smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))
