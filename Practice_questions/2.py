s = "programming"
d = {}

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for i in s:
    if d[i] == 1:
        print("First non-repeating character:", i)
        break
else:
    print("No non-repeating character")