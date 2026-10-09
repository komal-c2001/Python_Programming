list = [1,"komal",2,"harshika",6,"Bhavya",3]
s = max(x for x in range(len(list)))
for i in range(len(list)):
    if(list[i] == s):
        index = i
print(list[:index])
print(list[index::])
print(s)