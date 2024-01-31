a = int(input("Enter first number :- "))
b = int(input("Enter Second number :- "))
c = int(input("Enter Third number :- "))

largest = 0

if(a>b)and(a>c):
    largest = a
elif(b>c):
    largest = b
else:
    largest = c
    
print("Largest Number is ",largest)