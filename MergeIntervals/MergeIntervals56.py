from typing import List


class MergeIntervals:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        first = 0
        newIntervals = [intervals[0]]
        for i in range(1, len(intervals)):
            if newIntervals[first][1] >= intervals[i][0]:
                newIntervals[first][1] = max(newIntervals[first][1], intervals[i][1])
            else:
                newIntervals.append(intervals[i])
                first += 1
        return newIntervals


if __name__ == '__main__':
    merge = MergeIntervals()
    print(merge.merge([[1, 3], [2, 6], [8, 10], [15, 18]]), 'Expected: [[1, 6], [8, 10], [15, 18]]')
