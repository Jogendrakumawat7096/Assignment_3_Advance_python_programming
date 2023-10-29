# Write a Python program to read first n lines of a file.

def first_n_line(filename,n):
    file = open(filename,"r")
    for i in range(n):
        line =file.readline()
        print(line)
    


first_n_line("file.txt",2)
