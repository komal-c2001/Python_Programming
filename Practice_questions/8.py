arr = [1,2,3,4,5,6,7]
r = 3
k = r
while r > 0:
    i = 0 
    j = 1
    while j < len(arr):
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp
        j += 1
    r -= 1
print("Right Rotate array in ",k," times :",arr)
