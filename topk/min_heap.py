class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, num: int):
        self.heap.append(num)
        self.heapify_up(len(self.heap)-1)


    def remove_smallest(self):
        if len(self.heap) < 1:
            return  None
        if len(self.heap) == 1:
            return self.heap.pop()

        smallest = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return smallest

    def heapify_up(self, i: int):
        parent = (i-1) // 2
        if parent > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self.heapify_up(parent)

    def heapify_down(self, i: int):
        left = i * 2 + 1
        right = i * 2 + 2
        smallest = i
        if left < len(self.heap)-1 and  self.heap[left] < self.heap[i]:
            smallest = left

        if right < len(self.heap)-1 and self.heap[right] < self.heap[i]:
            smallest = right

        if smallest != i:
            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
            self.heapify_down(smallest)


if __name__ == '__main__':
    min_heap = MinHeap()
    min_heap.insert(5)
    min_heap.insert(3)
    min_heap.insert(8)
    min_heap.insert(1)

    for i in min_heap.heap:
        print(i)