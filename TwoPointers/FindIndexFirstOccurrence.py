

class FindFirstOccurrence:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                first = i
                j = 0
                while j < len(needle) and i < len(haystack) and haystack[i] == needle[j]:
                    i += 1
                    j += 1
                if j == len(needle):
                    return first
                
        return -1


if __name__ == '__main__':
    solution = FindFirstOccurrence
    print(solution.strStr(solution,"sadbutsad", "sad"))
    print(solution.strStr(solution,"leetcode", "leeto"))