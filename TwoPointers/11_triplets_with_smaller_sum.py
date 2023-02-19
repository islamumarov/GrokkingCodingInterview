class triplets_with_smaller_sum:
    def count_of_triplets(self, arr, target):
        arr.sort()
        count = 0
        for i in range(len(arr) - 2):
            count += self.search_pair(arr, target - arr[i], i)
        return count

    def search_pair(self, arr: [], target_sum: int, i: int) -> int:
        count = 0
        left, right = i + 1, len(arr) - 1
        while left < right:
            if arr[left] + arr[right] < target_sum:
                count += right - left
                left += 1
            else:
                right -= 1

        return count


if __name__ == '__main__':
    solution = triplets_with_smaller_sum()
    print(solution.count_of_triplets([-1, 4, 2, 1, 3], 5))
