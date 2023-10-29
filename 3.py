# Write a Python program to append text to a file and display the text. 

file = open("file.txt","a")
file.write("Jogendra Kumawat \n")
file.close()

file = open("file.txt","r")
j=file.read()
print(j)
file.close()