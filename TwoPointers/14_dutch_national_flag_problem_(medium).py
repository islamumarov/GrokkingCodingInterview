class Dutch_National_Flag_Problem:
    def in_place_sort(self, arr):
        low, high = 0, len(arr)-1
        i =0
        while i <= high:
            if arr[i] == 0:
                arr[i], arr[low] = arr[low], arr[i]
                i +=1
                low +=1
            elif arr[i] == 2:
                arr[i], arr[high] = arr[high], arr[i]
                high -=1
            else:
                i +=1
        return arr


if __name__ == '__main__':
    solution = Dutch_National_Flag_Problem()

    print(str(solution.in_place_sort([2, 2, 0, 1, 2, 0])))
    print(str(solution.in_place_sort([1, 0, 2, 1, 0])))
