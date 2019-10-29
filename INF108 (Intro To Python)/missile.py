#INF 108 - Module 2 Assignment 2

#Determine the distance (in km) a surface-to-air missile must travel to reach a given height and angle.
#distance = height / sin(angle)
#Note: the angle must be in radians; prompt for the angle in degrees and use this formula to convert:
#radians= (pi/180 degrees) * angle

import math

#Ask for user inputs
height = input("Enter the height (in km) you want your missile to reach: ")
angle = input("Enter the angle (in degrees) you want your missile to reach: ")


#Convert variables
height = float(height)
angle = float(angle)

#Convert from Degrees to Radians
radians = float((math.pi/180) * angle)


#Calculate distance
distance = float(height / (math.sin(radians)))


#Print the result
print("\n")
print("In order to achieve your goal, your missile needs to travel ", distance, " km.")
