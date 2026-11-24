arr = [1,2,3,4,5,6,7]
r = 3
k = r
while r > 0:
    i = 0
    j = len(arr)-1
    while j >= 0:
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp
        j -= 1
    r -= 1
print("left Rotate array in ",k," times :",arr)
