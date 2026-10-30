def number(*args):
    l = 0
    sl = 0
    for i in range(len(args)):
        if l < args[i]:
            sl = l
            l = args[i]
        if args[i] < l and sl != args[i]:
            sl = args[i]
    return sl
print("Second largest number = ",number(12,38,29,56,38,49,52))