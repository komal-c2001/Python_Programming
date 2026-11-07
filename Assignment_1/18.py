a = [1, 2, 3, 2, 4, 1, 5, 2]

d = {}

for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print("Duplicate numbers and their occurrences:")

for i in d:
    if d[i] > 1:
        print(i, "=", d[i], "times")