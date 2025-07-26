class Heap:
    def __init__(self, comparator):
        self.arr = []
        self.comparator = comparator


    def _heapify_down(self, k):
        