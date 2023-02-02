def remove_duplicates(arr):
    duplicates = 0
    first, second = 0, 1
    for i in range(1, len(arr)):
        if arr[i] == arr[first]:
            duplicates += 1
        first = i
    return len(arr) if duplicates == 0 else len(arr) - duplicates


if __name__ == '__main__':
    print(str(remove_duplicates([2, 3, 3, 3, 6, 9, 9])))
    print(str(remove_duplicates([2, 2, 2, 11])))
