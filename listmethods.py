a= [1,2,3,6]
b=[7,5,3]
c=["green","pink","blue"]
print(min(a))
print(max(b))
print(len(a))

a.insert(3,'abc')
print(a)

a.append ('mko')
print(a)

a.extend(b)
print(a)

c.sort()
print(c)

a.remove(2)
print(a)

a.reverse()
print(a)

a.pop()
print(a)

b.pop(2)
print(a)



#tuple is coverted in list
tuple = (231,"pqr","red","blue")
alist = list(tuple)
print(alist)
