from heapq import heappush, heappop


class MedainOfStream:
    max_heap = []
    min_heap = []

    def inser_num(self, num: int):

        if not self.max_heap or self.min_heap and -self.min_heap[0] >= num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self):

        if len(self.min_heap) == len(self.max_heap):
            return -self.max_heap[0] / 2.0 + self.min_heap[0] / 2.0
        else:
            return -self.max_heap[0] / 1.0


if __name__ == '__main__':
    medianSolver = MedainOfStream()

    medianSolver.inser_num(1)
    medianSolver.inser_num(3)

    print(medianSolver.findMedian())
    medianSolver.inser_num(5)
    print(medianSolver.findMedian())
    medianSolver.inser_num(4)

    print(medianSolver.findMedian())
