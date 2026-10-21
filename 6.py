list = [1,"komal",2,"harshika","Bhavya",3]
list.insert(3,4)
list.insert(4,8)
list.append("raj")
s = max(x for x in list if isinstance(x,(int)) and not isinstance(x,bool))
for i in range(len(list)):
    if(list[i] == s):
        break
print(list[:i])
print(list[i::])
print(s)