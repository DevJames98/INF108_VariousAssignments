#Write a graphics program to calculate the cost per square inch of a circular pizza. Accept as input the diameter (in inches) and pizza price. Print the cost per square inch. If the cost per square inch is more than $.10 print a message that informing the user that this pizza is too expensive. Otherwise let the user know this is a good deal!

#import everything from the graphics library
from graphics import *
import math

def main():
    #Create window
    pizza = GraphWin("Pizza Cost", 600, 400)

    #Ask for user inputs
    Text(Point(150,10), "Enter the diameter (in inches) of your pizza:").draw(pizza)
    input1 = Entry(Point(300,15),5)
    input1.draw(pizza)

    Text(Point(150,30), "Enter the price of your pizza:").draw(pizza)
    input2 = Entry(Point(300,35),5)
    input2.draw(pizza)

    #Create button for calculations
    button = Text(Point(200,100), "Calculate Cost per Square Inch")
    button.draw(pizza)
    Rectangle(Point(115,75),Point(285,125)).draw(pizza)

    #Create output texts
    output1 = Text(Point(150,160), "")
    output1.draw(pizza)

    output2 = Text(Point(150,190), "")
    output2.draw(pizza)

    #Wait for user to click button
    pizza.getMouse()

    #Calculate cost per square inch
    diameter = input1.getText()
    price = input2.getText()

    diameter = float(diameter)
    radius = float(diameter/2)
    price = float(price)
    #Price / (Area of a Circle -- Pi * r^2) (not sure if this formula is correct)
    cps = float(price/ (math.pi * pow(radius,2)))

    #Print cost per square inch
    output1.setText("Cost per Square Inch: $" + str(cps))


    #Print statement based on the cost per square inch
    high = "Your pizza is too expensive!"
    low = "This is a good pizza deal!"

    if cps > .10:
        output2.setText(high)
    else:
        output2.setText(low)

    #Close after next click
    pizza.getMouse()
    pizza.close()


main()
