a = [100, 4, 200, 1, 3, 2, 5]

s = set(a)
longest = 0
start = 0

for i in s:
    if i - 1 not in s:
        count = 1
        temp = i

        while temp + 1 in s:
            temp += 1
            count += 1

        if count > longest:
            longest = count
            start = i

print("Longest consecutive sequence:")

for i in range(start, start + longest):
    print(i, end=" ")

print("\nLength =", longest)