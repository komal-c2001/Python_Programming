with open("one.txt") as f:
    lines = f.readlines()
    print("2nd line of the file =" , lines[1])
    print("4th line of the file =",lines[3])
    print("Total Lines of the file = ",len(lines))