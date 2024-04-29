def fruits_into_baskets(fruits):
    window_start = 0
    baskets = {}
    max_len = -1
    for i, j in enumerate(fruits):
        if j in baskets:
            baskets[j] += 1
        else:
            baskets[j] = 1
        while len(baskets) >= 2:
            baskets[fruits[window_start]] -= 1
            if baskets[fruits[window_start]] == 0:
                del baskets[fruits[window_start]]
            window_start += 1
        max_len = max(max_len, i - window_start + 1)



if __name__ == '__main__':
    print("Max fruits in baskets " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Max fruits in baskets " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))
