import functools
numbers = [1,2,3,4,5,6,7,8,9,10]
square = list(map(lambda x:x**2 , numbers))
print("Squares = ",square)
Even = list(filter(lambda x:x%2==0 , numbers))
print("Even numbers = ",Even)
sum = functools.reduce(lambda x,y:x+y,numbers)
print("Sum = ",sum)