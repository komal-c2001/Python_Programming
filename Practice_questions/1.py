a = [10, 20, 5, 40, 30, 10]

largest = second_largest = float('-inf')
smallest = second_smallest = float('inf')

for i in a:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

    if i < smallest:
        second_smallest = smallest
        smallest = i
    elif i < second_smallest and i != smallest:
        second_smallest = i

print("Second largest:", second_largest)
print("Second smallest:", second_smallest)