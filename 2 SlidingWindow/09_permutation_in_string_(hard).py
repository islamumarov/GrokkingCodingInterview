import queue


def find_permutation(str1, str2):
    window_start = 0
    dic = {}
    for i, j in enumerate(str2):
        dic[j] = dic.get(j, 0) + 1
    for i, j in enumerate(str1):
        if j not in str2:
            window_start += 1
            continue
        if (i - window_start + 1) == len(str2):
            tmpDic = dic.copy()
            for s, k in enumerate(str1[window_start:i + 1]):
                if k in tmpDic:
                    tmpDic[k] -= 1
                    if tmpDic[k] == 0:
                        tmpDic.pop(k)
            if len(tmpDic) == 0:
                return True

            window_start += 1

    return False



if __name__ == '__main__':
    print(find_permutation('oidbcaf', 'abc'))
    print(find_permutation("bcdxabcdy", "bcdxabcdy"))
    print(find_permutation("aaacb", "abc"))
    print(find_permutation("eidboaoo", "ab"))
    print(find_permutation("ccccbbbbaaaa", "abc"))
    print(find_permutation("ainwkckifykxlribaypk", "ky"))

    print('--------------------------------------------------------------')
