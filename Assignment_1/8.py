print(bool([]),bool('0'),bool(0))
x = 10
if x > 5:
    pass
else:
    print('A')
print('B')
a = [1, 2]
b = [1, 2]
print(a == b, a is b)
x = [i for i in range(6) if i % 2 == 0]
print(x)
d = {'a': 1, 'b': 2}
print(d.get('c', 5))

x = 'Python'
print(x[1:5:2])

a = (1, 2, [3, 4])
a[2].append(5)
print(a)
x = 5
print(x > 3 and x < 5 or x == 5)

def f(x, items=[]):
    items.append(x)
    return items
print(f(1))
print(f(2))

print(list(filter(lambda x: x % 2, range(6))))

print('banana'.replace('a', 'X', 2))

g = (x * x for x in range(3))
print(next(g))
print(next(g))

print(list(zip([1, 2, 3], ['a', 'b'])))