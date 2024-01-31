lowerValue = int(input ("Enter the Lowest Range Value: "))  
upperValue = int(input ("Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for number in range (lowerValue, upperValue + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)