class triplets_sum_to_zero:
    def search_triplets(self, arr):
        arr.sort()
        triplets = []
        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            self.find_triplets(arr, -arr[i], i+1, triplets)
        return triplets


    def find_triplets(self, arr, target_sum, left, triplets):
        right = len(arr)-1
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target_sum:
                triplets.append([-target_sum, arr[left], arr[right]])
                left +=1
                right -=1
                while left < right and arr[left] == arr[left-1]:
                    left +=1
                while left < right and arr[right] == arr[right + 1]:
                    right -=1
            elif current_sum > target_sum:
                right-=1
            else:
                left +=1