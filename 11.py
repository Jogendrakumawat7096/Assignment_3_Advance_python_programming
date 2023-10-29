# Write a Python program to write a list to a file

list=["jogendra ","Kumawat","Tops Technology"]

def write_list_to_file(filename,lst):
    file =open(filename,"a")
    for items in lst:
        file.write(f"{items}\n")
        
write_list_to_file("file.txt",list)