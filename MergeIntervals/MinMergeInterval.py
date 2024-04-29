from typing import List


class MinMergeIntervals:
    def merge(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        first = 0
        newIntervals = [intervals[0]]
        for i in range(1, len(intervals)):
            if newIntervals[first][1] > intervals[i][0]:
                min_interval = min(newIntervals[first][1], intervals[i][1])
                newIntervals[first][1] = min_interval
            else:
                newIntervals.append(intervals[i])
                first += 1
        return len(intervals) - len(newIntervals)

if __name__ == "__main__":
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    intervals2 = [[1, 2], [1, 2], [1, 2]]
    intervals3 = [[1,2],[2,3]]
    print(MinMergeIntervals().merge(intervals))
    print(MinMergeIntervals().merge(intervals2))
    print(MinMergeIntervals().merge(intervals3))
