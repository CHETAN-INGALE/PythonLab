a = int(input("Enter first number :- "))
b = int(input("Enter Second number :- "))
c = int(input("Enter Third number :- "))

smallest= 0

if(a<b)and(a<c):
    smallest = a
if(b<a)and(b<c):
    smallest = b
if(c<a)and(c<b):
    smallest = c
    
print("Smallest Number is ",smallest)