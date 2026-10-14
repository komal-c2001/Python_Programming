with open("one.txt") as f:
    s = f.read()
    count = 0
    for i in s:
        if i in "AEIOUaeiou":
            count += 1
    print("Total count of vowels in the file = ",count)