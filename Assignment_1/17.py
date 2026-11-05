n = 153
temp = n

# Count number of digits
count = 0
while temp > 0:
    count += 1
    temp = temp // 10

temp = n
total = 0

# Calculate Armstrong sum
while temp > 0:
    digit = temp % 10
    total = total + digit ** count
    temp = temp // 10

if total == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")