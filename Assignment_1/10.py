def generator(n):
    for i in range(1,n+1):
        yield i
def display():
    for i in generator(30):
        if(i % 2 == 0):
            print(i,end=" ")
print("All even number")
display()