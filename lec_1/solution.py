q1# take an input from user is should be a number and find out how many digit it has

#taking input form user 
n=int(input("Enter number:"))
count=0
#using while loop
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number are:",count)



q2# take an input from the user the factorial of a number if the user enters a string print not a valid input

# Define a function named factorial
def factorial(a):
    if a == 0:
        # If a is 0 then return 1
        return 1
    else:
        # If a is not 0
        return a * factorial(a - 1)

# Ask the user to input a number
a = int(input("Enter the value factorial: "))
print(factorial(a))


    
