num = int(input("Enter a number="))
for i in range(1,num+1):
    for s in range(num-i,0,-1):
        print(" ",end="")
    for j in range((2*i)-1,0,-1):
        if(i % 2 == 0):
            print("#",end="")
        else:
            print("*",end="")
    print()