def number(*args):
    freq = {}
    for i in args:
        if i in freq:
            freq[i]  += 1
        else:
            freq[i] = 1
    return freq
print("Count Occurence of number using multiple argument",number(2,1,4,6,2,7,8,9,1,3,5,8))