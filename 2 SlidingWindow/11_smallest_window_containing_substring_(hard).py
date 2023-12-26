class Solution:
    def find_substring(self, s, t):
        s_dict, t_dict = {}, {}
        min_window = s+"1"
        if len(s) < len(t):
            return ""
        for i in range(len(t)):
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
        l = 0
        for r in range(len(s)):
            r_char = s[r]
            if r_char in t_dict:
                s_dict[r_char] = 1 + s_dict.get(r_char, 0)

                if len(s_dict) == len(t_dict):
                    while self.contain_str(s_dict, t_dict):
                        current = s[l:r + 1]
                        min_window = min_window if len(min_window) < len(current) else current
                        if s[l] in s_dict:
                            s_dict[s[l]] -= 1
                            if s_dict[s[l]] == 0:
                                del s_dict[s[l]]
                        l += 1

        return "" if len(min_window) > len(s) else min_window

    def contain_str(self, s_dict, t_dict) -> bool:
        for i, j in enumerate(t_dict):
            if t_dict[j] > s_dict.get(j, 0):
                return False
        return True


if __name__ == '__main__':
    print(find_substring("aa", "aa"))
    print(find_substring("ADOBECODEBANC", "ABC"))
