
#Task 1
# Print numbers from 10 to 200 using the while loop
# Your numbers must be in multiples of 10.
# 10 must be first number printed, and 200 the last number.

# Example: 10, 20, 30 ..... 180, 190, 200.
# Note that the numbers do not need to be printed in one line.
# Write your code here
#ra = range(9,200,10) # code here is not correct... don't use this
# a range() usually used in a for loop

# while loop is a loop with a condition
# as long as the condition is true, it will loop


skibidi=10 #start numb

while skibidi < 210:
    print(skibidi)
    skibidi=skibidi+10




###################################################

# Task 2
# Code a password checker to protect your code!

# Assign a password "superpass123" to a variable
# Ask the user to enter a password
# If the password matches, print “Access Granted”
# If the password does not match, print “Access Denied”

# Write your code here


HiddenPass = "superpass123"
#Hidden Password

PasswordGuessed=input("What is the password? ")
# ask for pass
if PasswordGuessed == HiddenPass:
    print("Access Granted")
else:
    print("Access Denied")
#checking password
##########################################