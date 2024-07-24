class FibonacciNumber:
    def fib(self, n: int) -> int:
        sequence = [0, 1]
        i = len(sequence)

        # trivial case
        while i <= n:
            results = sequence[i - 1] + sequence[i - 2]
            sequence.append(results)
            i += 1

        return sequence[n]



if __name__ == '__main__':
    sol = FibonacciNumber()
    print(sol.fib(10))
