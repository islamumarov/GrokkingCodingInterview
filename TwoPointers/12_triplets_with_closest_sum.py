class triplets_with_closest_sum:
    def search_triplet(self, arr: [], target):
        arr.sort()
        smallest_diff = float('inf')
        for i in range(len(arr) - 2):
            left, right = i + 1, len(arr) - 1
            while left < right:
                target_diff = target - arr[i] - arr[left] - arr[right]
                if target_diff == 0:
                    return target - target_diff
                if abs(target_diff) < abs(smallest_diff):
                    smallest_diff = target_diff

                if target_diff > 0:
                    left += 1
                else:
                    right -= 1

        return target - smallest_diff


if __name__ == '__main__':
    solution = triplets_with_closest_sum()
    print(solution.search_triplet([-1, 2, 1, -4], 1))
    print(solution.search_triplet([-1000, -1000, -1000], 10000))
