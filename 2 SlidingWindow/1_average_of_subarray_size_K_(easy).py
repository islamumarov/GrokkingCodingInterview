def find_averages_of_subarrays(arr, K):
    result = []
    start_window, window_sum = 0, 0.0
    for end_window in range(len(arr)):
        window_sum += arr[end_window]
        if end_window - start_window >= K - 1:
            result.append(window_sum / 5)
            window_sum -= arr[start_window]
            start_window += 1
    return result


if __name__ == '__main__':
    print('Averages of subarrays of size K: ' + str(find_averages_of_subarrays([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)))
