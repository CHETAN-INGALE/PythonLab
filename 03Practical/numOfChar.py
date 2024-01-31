f = open("text.txt", "r")

content = f.read()

num_chars = len(content)

print("The number of characters in the file is:", num_chars)

f.close()