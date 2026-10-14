with open("one.txt") as f:
    s = f.read()
    words = s.split()
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    print("Unique words =", unique_words)
