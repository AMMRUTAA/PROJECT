mydic={1:'apple',2:'ball',3:'cat'}
mydic1={'name':'era',1:[3,4,5]}
mydic2=dict({1:'apple',2:'ball',3:'cat'})
mydic3=([(1,'apple'),(2,'ball')])
mydic4={} #empty dictionary
print (mydic)
print()
print (mydic1)
print()
print (mydic2)
print()
print (mydic3)
print()
print (mydic4)

#Accessing Dictionary elements
mydict={'name':'swara','age':7,'class':'fifth'}
print("Name :",mydict ['name'])
print("Age :",mydict ['age'])
print("Class :",mydict ['class'])
#in case of duplictae assign last value will be displayed
mydict={'name':'swara','age':7,'class':'fifth'}
print("Name :",mydict ['name'])

#Appemding elements to dictionary
mydict={'name':'swara','age':7,'class':'fifth'}
print (mydict)
mydict ['age']=8
print (mydict)
mydict['name']='pooja'
print (mydict)
print()
print()

#traversing elements to dictionary
mydict = {'name':'swara','age':7,'class': 'fifth'}
for k in mydict:
    print(k)
print()
print()
for k,v in mydict.items():
    print(k,v)

# dictionary update delete
mydict4 = {'name': 'riya', 'age': 21}
print(mydict4)

newdict4 = {'fav_food': 'pavbhaji'}
mydict4.update(newdict4)

print(newdict4)
print(mydict4)

print()
print(mydict4)

del mydict4['name']
print(mydict4)

mydict4.clear()
print(mydict4)

del(mydict4)
print(mydict4)
