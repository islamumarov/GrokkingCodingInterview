class LongestSubstringWithoutRepeat:
    def findLengthOfLongestSubstring(self, s: str):
        first = 0
        max_len = 0
        dict = {}
        for i, j in enumerate(s):
            while j in dict:
                dict[s[first]] -= 1
                if dict[s[first]] == 0:
                    del dict[s[first]]
                first += 1
            dict[j] = 1
            max_len = max(max_len, i - first+1)

        return max_len



if __name__ == '__main__':
    sol = LongestSubstringWithoutRepeat()

    print(sol.findLengthOfLongestSubstring("abcabcbb"))
    print(sol.findLengthOfLongestSubstring("pwwkew"))
