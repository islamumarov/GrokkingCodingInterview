def search(arr, target_sum):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [left, right]
        if target_sum > current_sum:
            left += 1
        else:
            right -= 1
    return [-1, -1]

if __name__ == '__main__':
    print(str(search([2, 7, 11, 15], 9)))
    print(str(search([1, 2, 3, 4, 6], 6)))
    print(str(search([2, 5, 9, 11], 11)))

