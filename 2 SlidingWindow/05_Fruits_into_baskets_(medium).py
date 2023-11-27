def fruits_into_baskets(fruits):
    baskets = {}
    max_fruits = -1
    window_start = 0
    for i, j in enumerate(fruits):
        if j not in baskets:
            baskets[j] = 1
        else:
            baskets[j] += 1
        while len(baskets) > 2:
            baskets[fruits[window_start]] -= 1
            if baskets[fruits[window_start]] == 0:
                del baskets[fruits[window_start]]
            window_start += 1
        max_fruits = max(max_fruits, i - window_start + 1)
    return max_fruits

if __name__ == '__main__':
    print("Max fruits in baskets " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Max fruits in baskets " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))
