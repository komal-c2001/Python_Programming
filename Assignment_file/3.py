sent = input("Enter a sentence = ")
list = sent.split(" ")
print("Display word =",list)
print("Longext word in sentence = ",max(list,key=len))