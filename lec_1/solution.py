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



#.isalpha()

q3# create a program

Computers ={
  "Laptop1" : {"brand" : "DELL","OS" : "Windows"},
  "Laptop2" : {"brand" : "HP", "OS" : "Linux"},
  "Desktop" : {"brand" : "Apple","OS" : "Mac-OS"}
}
# from this above data create a list brand,OS
#print(brand)
#['brand','hp','apple']
#print(os)
#['Windows','Linux','MAc-os']


Computers ={
  "Laptop1" : {"brand" : "DELL","OS" : "Windows"},
  "Laptop2" : {"brand" : "HP", "OS" : "Linux"},
  "Desktop" : {"brand" : "Apple","OS" : "Mac-OS"}
}
brand = []
os = []
for laptop, key in Computers.items():
    brand.append(key["brand"])
    os.append(key["OS"])
print(brand)
print(os)






Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

class Solution(object):
    def twoSum( self, nums, target):
    
        for i, in range(0, len(nums)):
            for j, in range(i+1, len(nums)):
                
                
                if(nums[i]+nums[j]==target):
                    return [i,j]
        return []

    
