#Devon James INF 108 Module 2 - highwayTax.py

#   Full market house values are estimated by the user
#   The assessed value of a house is 90% of full market value
#   Highway taxes are 0.00079 of the assessed value
#-----------------------------------------------------------------------------
#Task: Write a program that asks the user to enter a house value. The program will calculate and print the highway tax.


#Ask for user inputs
houseValue = input("Enter the current estimated house value: ")


#Convert variables
houseValue = float(houseValue)
assessedValue = float(houseValue * 0.9)

#Calculate highwayTax
highwayTax = float(assessedValue * 0.00079)


#Print the result
print("The highway taxes are: $", highwayTax)
