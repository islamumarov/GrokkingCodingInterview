from typing import List

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
