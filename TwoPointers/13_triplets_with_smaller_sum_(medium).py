import unittest

class triplets_with_smaller_sum:
    def find_triplets(self, arr, target):
        count = 0
        arr.sort()
        for i in range(len(arr)-2):
            count += self.search_pair(target - arr[i], arr, i)
        return count

    def search_pair(self, target, arr, i):
        left, right = i+1, len(arr)-1
        count = 0
        while left < right:
            sum = arr[left] + arr[right]
            if sum < target:
                count += right - left
                left += 1
            else:
                right -= 1
        return count

if __name__ == '__main__':
    solution = triplets_with_smaller_sum()

    assert solution.find_triplets([-1, 4, 2, 1, 3], 5) == 4
