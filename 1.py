print("Table of all odd numbers from 1 to 10")
for i in range(1,11):
    for j in range(1,11):
        if i % 2 == 1:
            print(i*j,end=" ")
    print()