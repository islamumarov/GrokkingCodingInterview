class MinimumRemoveMakeValidParentheses:
    def minRemoveValid(self, s: str) -> str:
        stack = {}
        n = len(s)
        i = 0
        while i < n:
            if s[i] == '(':
                if s[i] not in stack:
                    stack[s[i]] = []
                stack[s[i]].append(i)
            elif s[i] == ')':
                if '(' in stack:
                    stack['('].pop()
                    if len(stack['(']) == 0:
                        del stack['(']
                else:
                    s = s[:i] + s[i + 1:]
                    i -= 1
                    n -= 1
            i += 1

        while '(' in stack and len(stack['(']) > 0:
            i = stack['('].pop()
            s = s[:i] + s[i + 1:]
        while ')' in stack and len(stack[')']) > 0:
            i = stack[')'].pop()
            s = s[:i] + s[i + 1:]
        return s


if __name__ == '__main__':
    print(MinimumRemoveMakeValidParentheses.minRemoveValid(MinimumRemoveMakeValidParentheses, "(a(b(c)d)"))
