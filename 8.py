# Write a python program to find the longest words. 

def find_longest_words(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

# Call the function
longest_words = find_longest_words('file.txt')
print(longest_words)

