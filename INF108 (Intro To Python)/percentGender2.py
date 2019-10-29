#Asks the user for the number of males and females registered in class and display the percentages of males & females in the class

#import everything from the graphics library
from graphics import *

#Create window
newWin = GraphWin("Percent Gender Calculator", 800, 600)

#Ask for user input
numOfMales = Text(Point(200,20), "Enter the number of registered males in your class:")
numOfMales.draw(newWin)

#Textbox for user to enter input
aRectangle = Entry(Point(100,40), 5)
aRectangle.draw(newWin)

#Ask for user input
numOfFemales = Text(Point(200,60), "Enter the number of registered females in your class:")
numOfFemales.draw(newWin)

#Textbox for user to enter input
bRectangle = Entry(Point(100,80), 5)
bRectangle.draw(newWin)

#Checks to see if user clicked on window and stores point in variable
#(tried to find a way/function to determine if this can be expressed as a boolean instead of returning the point value location)
click = newWin.getMouse()
if click == true
    #Once user clicks, gets values from inputs to perform calculations
    m = aRectangle.getText()
    f = bRectangle.getText()


#Convert variables
m = int(m)
f = int(f)


#Percentage variables for Male/Female as floating point numbers
mPercent = 1.0
fPercent = 1.0
mPercent = float(mPercent)
fPercent = float(fPercent)

#Calculate percentages
total = m + f
mPercent = (m / total) * 100
fPercent = (f / total) * 100


#Print the result
print1 = Text(Point(200,100), "Percentage of Males: ", mPercent, "%"")
print1.draw(newWin)
print2 = Text(Point(200,120), "Percentage of Females: ", fPercent, "%"")
print2.draw(newWin)
