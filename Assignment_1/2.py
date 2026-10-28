list = [1,"komal",2,"harshika",8,"Bhavya",3]
s = max(x for x in list if isinstance(x,(int)) and not isinstance(x,bool))
for i in range(len(list)):
    if(list[i] == s):
        break
print(list[:i])
print(list[i::])
print(s)