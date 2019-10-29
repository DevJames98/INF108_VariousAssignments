#INF 108 - Module 2 Assignment 1 Pt. 1
#Accept as input the 3 dimensions of a box (length, width, and height) and calculate the volume

#Ask for user input
length = input("Enter the length of the box: ")
width = input("Enter the width of the box: ")
height = input("Enter the height of the box: ")

#Convert to float numbers (in case there are decimals involved)
length = float(length)
width = float(width)
height = float(height)

#Calculate volume
volume = length * width * height

#Print the result
print("The volume of this box is: ", volume)
