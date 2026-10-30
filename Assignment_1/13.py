def display(num):
    count =  0
    while(num > 0):
        count += 1
        num = num // 10
    return count
print("Count digit of given number =",display(124536))