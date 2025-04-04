f =open("myfile.txt","r")
text=f.read()
print("\n",text)

f=open("myfile.txt","a")
f.write("\n I am the new appending text1")
f.close()
print()
print()
       
print("After appending the content")
f=open("myfile.txt","r")
text=f.read()
print(text)       
       
