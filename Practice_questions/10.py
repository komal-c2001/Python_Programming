arr =[910,910,920,920,920, 930, 930, 930, 940, 950,910, 960, 950, 960, 940, 990, 980, 980, 970, 970, 1000, 1000, 1000, 1000]
def countFrequency(arr):
    arr1 = [0] * 101
    i = 0
    j = 0
    for i in range(len(arr)):
        for j in range(len(arr1)):
            if (arr[i] - 900) == j:
                arr1[j] += 1
                break
    return arr1
print("Frequency Array Using Index Mapping :",countFrequency(arr))