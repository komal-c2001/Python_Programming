s1 = "listen"
s2 = "silent"

d = {}

for i in s1:
    d[i] = d.get(i, 0) + 1

for i in s2:
    d[i] = d.get(i, 0) - 1

if all(value == 0 for value in d.values()) and len(s1) == len(s2):
    print("Anagram")
else:
    print("Not Anagram")