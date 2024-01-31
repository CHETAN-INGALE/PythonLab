
f = open("text.txt", "r")

count = 0

for line in f:
  if line.startswith("Humpty"):
    count += 1

print("The number of lines that start with Humpty is:", count)

f.close()