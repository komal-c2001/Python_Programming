with open("one.txt") as f:
    s = f.read()
    list = s.split()
    print("Total number of words in the file = ",len(list))