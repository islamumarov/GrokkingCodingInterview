
if __name__ == '__main__':
    happy_num = happy_number()
    print("expected: ", True, " Got: ", happy_num.find_happy_number(19))
    print("expected: ", False, " Got: ", happy_num.find_happy_number(2))
