class ValidPalindrome:
    def IsPalindrome(self, s: str):

        res = []
        for i, j in enumerate(s):
            if j.isalnum():
                res.append(j.lower())

        if len(res) < 1:
            return True
        if len(res) == 1:
            return False
        left = 0
        right = len(res)-1
        while right >= left:
            if res[left] != res[right]:
                return False
            left += 1
            right -= 1

        return True


if __name__ == '__main__':
    solution = ValidPalindrome()

    print(solution.IsPalindrome('0P'))
    print(solution.IsPalindrome('A man, a plan, a canal: Panama'))
