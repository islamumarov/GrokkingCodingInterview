from typing import List
import operator

def duplicateNumbersXOR(nums: List[int]) -> int:
    dict = {}
    duplicates = []
    for i, j in enumerate(nums):
        if j in dict:
            duplicates.append(j)
        else:
            dict[j] = 0
    if len(duplicates) < 1:
        return 0

    s = duplicates[0]
    for i in range(1, len(duplicates)):
        s = s ^ duplicates[i]
    return s



def occurrencesOfElement(nums: List[int], queries: List[int], x: int) -> List[int]:
    dict = {}
    res = []
    for i, j in enumerate(nums):

        if j in dict:
            dict[j].append(i)
        else:
            dict[j] = [i]

    for i, j in enumerate(queries):
        if x not in dict or len(dict[x]) <= j:
            res.append(-1)
        else:
            res.append(dict[x][j-1])

    if len(res) <= 0:
        return [-1]
    return res

if __name__ == '__main__':
    nums = [1,2,2,1]

    #print(duplicateNumbersXOR(nums))

    print(occurrencesOfElement([1,3,1,7],
[1,3,2,4],
1))

    print(
        occurrencesOfElement(
            [1, 2, 3],
            [10],
    5
        )
    )