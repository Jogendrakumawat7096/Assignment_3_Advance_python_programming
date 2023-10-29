# Write a Python program to read an entire text file

file = open("file.txt","w")
file.write("Jogendra Kumawat")
file.close()

file = open("file.txt","r")
j=file.read()
print(j)
file.close()