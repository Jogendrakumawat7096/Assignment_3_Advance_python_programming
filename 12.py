# Write a Python program to copy the contents of a file to another file. 

file = open("file.txt","r")
a =file.read()
file.close()

file1= open("file1.txt","w")
file1.write(a)
file1.close()

