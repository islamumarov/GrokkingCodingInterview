class PermutationInString:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm = {}
        n = len(s2)
        for j, i in enumerate(s1):
            if i in perm:
                perm[i] += 1
            else:
                perm[i] = 1

        for j, i in enumerate(s2):
            if i in perm and n-j-1 >= len(s1)-1:
                tmp = perm.copy()
                k = j
                while len(tmp) > 0 and s2[k] in tmp:
                    tmp[s2[k]] -= 1
                    if tmp[s2[k]] == 0:
                        del tmp[s2[k]]
                    k += 1

                if len(tmp) == 0:
                    return True

        return False



if __name__ == '__main__':
    sol = PermutationInString()
    print(sol.checkInclusion("adc", "dcda"))