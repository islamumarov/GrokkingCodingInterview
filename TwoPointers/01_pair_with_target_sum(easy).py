def search(nums, target):
    left, right = 0, len(nums)-1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left+1, right+1]
        if sum > target:
            right -= 1
        else:
            left += 1

    return [-1, -1]


if __name__ == '__main__':
    print(str(search([2, 7, 11, 15], 9)))
    print(str(search([1, 2, 3, 4, 6], 6)))
    print(str(search([2, 5, 9, 11], 11)))

