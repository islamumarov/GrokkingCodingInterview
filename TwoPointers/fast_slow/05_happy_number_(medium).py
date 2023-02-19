class happy_number:
    def find_happy_number(self, num):
        fast, slow = self.sum_of_digits_square(num), num
        while fast != 1 and fast != slow:
            slow = self.sum_of_digits_square(slow)
            fast = self.sum_of_digits_square(self.sum_of_digits_square(fast))
        return fast == 1

    def sum_of_digits_square(self, num):
        sum = 0
        while num > 0:
            tmp = num % 10
            sum += tmp * tmp
            num = num // 10
        return sum


if __name__ == '__main__':
    happy_num = happy_number()
    print("expected: ", True, " Got: ", happy_num.find_happy_number(19))
    print("expected: ", False, " Got: ", happy_num.find_happy_number(2))
