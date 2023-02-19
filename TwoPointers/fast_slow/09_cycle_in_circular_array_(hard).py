from typing import List


class cycle_in_circular_array:
    def circular_array_loop_exist(self, nums):

        for i in range(len(nums)):
            is_forward = nums[i] >= 0
            slow, fast = i, i

            while True:
                slow = self.find_next_index(nums, is_forward, slow)
                fast = self.find_next_index(nums, is_forward, fast)
                if fast != -1:
                    fast = self.find_next_index(nums, is_forward, fast)
                if slow == -1 or fast == -1 or slow == fast:
                    break
            if slow != -1 and slow == fast:
                return True

        return False

    def find_next_index(self, nums, is_forward, current_index):
        direction = nums[current_index] >= 0

        if is_forward != direction:
            return -1
        next_index = (current_index + nums[current_index]) % len(nums)
        if next_index == current_index:
            return -1
        return next_index

def addBinary(a: str, b: str) -> str:
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    res = ""
    while i >= 0 or j >= 0:
        if i >= 0:
            carry += int(a[i])
            i -= 1
        if j >= 0:
            carry += int(b[j])
            j -= 1
        res = str(carry % 2) + res
        #res *= 10
        carry = carry // 2

    if carry > 0:
        res = str(carry) + res
    return res


def addToArrayForm(self, num: List[int], k: int) -> List[int]:
    sum = 0
    list = []
    for i in num:
        sum *= 10
        sum += i
    sum +=k
    sum_string = str(sum)
    for i in sum_string:
        list.append(ord(i) - ord('0'))
    return list
if __name__ == '__main__':

    print(addBinary("11", "1"))
    print(addBinary("1010", "1011"))
    # solution = cycle_in_circular_array()
    # print(solution.circular_array_loop_exist([-1, -2, -3, -4, -5, 6]))
    # print(solution.circular_array_loop_exist([2, -1, 1, 2, 2]))
    # print(solution.circular_array_loop_exist([1, -1, 5, 1, 4]))
