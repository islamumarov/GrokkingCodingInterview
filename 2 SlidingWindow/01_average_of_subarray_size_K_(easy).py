
from typing import List

#Given an array, find the average of all contiguous subarrays of size ‘K’ in it.


def find_averages_of_subarrays(nums: List[int], k: int):
        avg = []
        window_start = 0
        window_sum = 0
        for i in range(0, len(nums)):
              window_sum += nums[i]
              if i - window_start+1 == k:
                    avg.append(window_sum/k)
                    window_sum -= nums[window_start]
                    window_start += 1
        
        return avg


if __name__ == '__main__':
    print('Averages of sub arrays of size K: ' + str(find_averages_of_subarrays([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)))
