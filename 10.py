# Write a Python program to count the frequency of words in a file

file = open("file.txt","r")
words =file.read().split()
freq_word = {}

for word in words:
    if word in freq_word:
        freq_word[word]+=1
    else :
        freq_word[word]=1    
for word,freq in freq_word.items():
    print(f"'{word}': {freq}")