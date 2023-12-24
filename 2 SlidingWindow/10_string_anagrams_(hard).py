def find_string_anagram(str1, str2):
    if len(str2) > len(str1):
        return []
    str1_dict, str2_dict = {}, {}
    for i in range(len(str2)):
        str2_dict[str2[i]] = 1 + str2_dict.get(str2[i], 0)
        str1_dict[str1[i]] = 1 + str1_dict.get(str1[i], 0)
    result = [0] if str2_dict == str1_dict else []
    window_start = 0
    for r in range(len(str2), len(str1)):
        str1_dict[str1[r]] = 1 + str1_dict.get(str1[r], 0)
        str1_dict[str1[window_start]] -= 1
        if str1_dict[str1[window_start]] == 0:
            del str1_dict[str1[window_start]]
        window_start += 1
        if str1_dict == str2_dict:
            result.append(window_start)

    return result

if __name__ == '__main__':
    print(find_string_anagram("abbcabc","abc"))
    print(find_string_anagram("ppqp","pq"))