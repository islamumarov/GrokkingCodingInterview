from typing import List

#Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

def max_sub_array_size_of_K(k, nums: List[int]):
    max_sum = float('-inf')
    window_start = 0
    window_sum = 0
    for i  in  range(0, len(nums)):
        window_sum += nums[i]
        if i - window_start + 1 == k: 
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[window_start]
            window_start += 1
    return max_sum


if __name__ == '__main__':
    print('Subarray [2, 1, 5, 1, 3, 2] maximum sum is ' + str(max_sub_array_size_of_K(3,[2, 1, 5, 1, 3, 2])) + '\n expexted: '+ str(9))
    print('Subarray [2, 3, 4, 1, 5] maximum sum is ' + str(max_sub_array_size_of_K(2,[2, 3, 4, 1, 5])) + '\n expexted: '+ str(7))


