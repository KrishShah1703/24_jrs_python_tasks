q1# take an input from user is should be a number and find out how many digit it has

#taking input form user 
n=int(input("Enter number:"))
count=0
#using while loop
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number are:",count)






    
