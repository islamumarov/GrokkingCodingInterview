def fruits_into_baskets(fruits):
    window_start = 0
    baskets = {}
    max_fruits = 0
    for window_end in range(len(fruits)):
        if fruits[window_end] not in baskets:
            baskets[fruits[window_end]] = 0
        baskets[fruits[window_end]] += 1
        while len(baskets) > 2:
            baskets[fruits[window_start]] -= 1
            if baskets[fruits[window_start]] == 0:
                del baskets[fruits[window_start]]
            window_start += 1
        max_fruits = max(max_fruits, window_end - window_start + 1)
    return max_fruits


if __name__ == '__main__':
    print("Max fruits in baskets " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Max fruits in baskets " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))
