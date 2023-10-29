# Write a Python program to read a file line by line and store it into a list



list = []
def first_n_line(filename,n):
    file = open(filename,"r")
    line =file.readlines()
    for i in line:
        list.append(i)
    
    print(list)    
           


first_n_line("file.txt",2)
