# Write a Python program to read last n lines of a file.

def read_last_n_lines(filename, n):
    with open(filename, 'r') as file:
        lines = file.readlines()
        last_n_lines = lines[-n:]
        for line in last_n_lines:
            print(line)

# Call the function
read_last_n_lines('file.txt', 4)
