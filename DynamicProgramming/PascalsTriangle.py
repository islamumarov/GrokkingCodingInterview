from typing import List


class PascalsTriangle:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        current = []
        col = 0
        while numRows-1 != col:
            n = len(result[col])
            for j in range(n+1):
                if j <= 0:
                    current.append(result[col][0])
                elif j == n:
                    current.append(result[col][0])
                else:
                    current.append(result[col][j-1] + result[col][j])
            result.append(current)
            current = []
            col += 1

        return result



if __name__ == '__main__':
    sol  = PascalsTriangle()

    print(sol.generate(5))