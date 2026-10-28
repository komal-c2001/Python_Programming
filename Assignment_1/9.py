def calculate(*args):
    total = 0

    def find_sum():
        nonlocal total

        for n in args:
            total += n

    find_sum()

    even = list(filter(lambda x: x % 2 == 0, args))

    print("Sum:", total)
    print("Even numbers:", even)


calculate(10, 15, 20, 25, 30)