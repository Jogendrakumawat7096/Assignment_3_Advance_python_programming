# Write a Python program to count the number of lines in a text file.

file = open("file.txt","r")
a =file.readlines()
print(len(a))
