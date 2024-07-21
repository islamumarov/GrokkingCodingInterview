from typing import List


class InsertInterval:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        first = 0
        ans = []
        if len(intervals) < 1:
            return [[newInterval[0], newInterval[1]]]
        if len(intervals) == 1:
            if intervals[0][0] <= newInterval[0] <= intervals[0][1] or newInterval[0] <= intervals[0][0] <= newInterval[1]:
                ans.append([min(intervals[0][0], newInterval[0]), max(intervals[0][1], newInterval[1])])
            elif intervals[0][0] < newInterval[0]:
                ans.append(intervals[0])
                ans.append([newInterval[0], newInterval[1]])
            else:
                ans.append([newInterval[0], newInterval[1]])
                ans.append(intervals[0])
            return ans
        while newInterval[0] > intervals[first][1] and first < len(intervals):
            first += 1

        for i in range(0, first+1):
            ans.append(intervals[i])
        ans.append([newInterval[0], newInterval[1]])
        ans.sort()
        for i in range(first, len(intervals)):
            ans.append(intervals[i])

        return self.merge(ans)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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
    intervals2 = [[1,5],[6,8]]
    newInterval2 = [0,9]
    intervals = [[1, 3], [6, 9]]
    intervals1 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [2, 5]
    newInterval1 = [4, 8]
    insert_interval = InsertInterval()

    print(insert_interval.insert(intervals2, newInterval2))
    print(insert_interval.insert(intervals, newInterval))
    print(insert_interval.insert(intervals1, newInterval1))