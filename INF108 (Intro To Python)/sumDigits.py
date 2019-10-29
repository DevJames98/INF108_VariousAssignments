#Devon James INF 108 Module 2 - sumDigits.py

#Write a program that ask the user to enter four single-digit numbers with nothing separating them. The program will display the sum of the four numbers entered.


#Ask for user inputs
digits = input("Enter four single-digit numbers with nothing separating them.")


#Convert variables
digits = int(digits)
sum = 0
sum = int(sum)

#Isolate digits
dList = list(digits)


#Calculate sum

for digits in dList:
    sum = sum + digits


#sum =

#Print the result
print("The sum of the entered digits is: ", sum)
