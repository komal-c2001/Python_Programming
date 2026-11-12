a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

maximum = a[0]
current = a[0]

for i in range(1, len(a)):
    current = max(a[i], current + a[i])
    maximum = max(maximum, current)

print("Maximum subarray sum:", maximum)