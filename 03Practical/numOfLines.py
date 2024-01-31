f = open("text.txt", "r")

lines = sum(1 for line in f)

print("The number of lines in the file is:", lines)

f.close()