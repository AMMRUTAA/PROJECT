# Corrected file path
file_path = r"C:\Users\Student\AppData\Local\Programs\Python\Python312\python\myfile.txt"

# Open the file in read mode
f = open(file_path, "r", encoding="utf-8")
text = f.read()
print("\n", text)
f.close()

# Open the file in append mode and write new content
f = open(file_path, "a", encoding="utf-8")
f.write("\n I am the new appending text1")
f.close()

# Reopen the file in read mode to display updated content
f = open(file_path, "r", encoding="utf-8")
print("\n\nAFTER APPENDING THE CONTENT")
text = f.read()
print(text)
f.close()
