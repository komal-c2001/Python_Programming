a = [2, 4, 3, 5, 7, 8, 1]
target = 9

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == target:
            print(a[i], a[j])