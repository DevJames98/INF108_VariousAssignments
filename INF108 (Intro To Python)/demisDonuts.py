#Write an GUI application for customers to place an order online. The user will select the donuts they want (five choices) and the quantity for each choice selected, then will select the coffee they want (and the quantity), then click on the ORDER button.
#The application interface will display the total of the order including a 7% sales tax added to the order. Include a message to the user telling them that the order is complete. Also draw, a small image using the graphics shapes we were introduced to in this module to the interface.
#The user will exit the GUI application by clicking on the QUIT button.

#import everything from the graphics library
from graphics import *

def main():

    #Create window
    donut = GraphWin("Demi's Donuts", 600, 800)

    #Set Coordinates to section out program
    donut.setCoords(0.0,0.0,6.0,12.0)

    #Welcome Message
    Text(Point(3,11), "Welcome to Demi's Donuts! Please select the items you'd like from our menu below:").draw(donut)

    Text(Point(3,10), "Donuts").draw(donut)

    #Draw Choice Buttons
    #--------------------------------------------------------------------------
    #Jelly Donut
    iJelly = Text(Point(1,9), "Jelly Donut")
    iJelly.draw(donut)
    Rectangle(Point(0.5,8.7),Point(1.4,9.3)).draw(donut)

    #Cream Donut
    iCream = Text(Point(2,9), "Cream Donut")
    iCream.draw(donut)
    Rectangle(Point(1.5,8.7),Point(2.4,9.3)).draw(donut)

    #Plain Donut
    iPlain = Text(Point(3,9), "Plain Donut")
    iPlain.draw(donut)
    Rectangle(Point(2.5,8.7),Point(3.4,9.3)).draw(donut)

    #Sugar Donut
    iSugar = Text(Point(4,9), "Sugar Donut")
    iSugar.draw(donut)
    Rectangle(Point(3.5,8.7),Point(4.4,9.3)).draw(donut)

    #Chocolate Donut
    iChoc = Text(Point(5,9), "Chocolate Donut")
    iChoc.draw(donut)
    Rectangle(Point(4.5,8.7),Point(5.5,9.3)).draw(donut)

    #--------------------------------------------------------------------------

    Text(Point(3,7), "Coffee").draw(donut)

    #Regular Coffee
    iReg = Text(Point(2,6), "Regular Coffee")
    iReg.draw(donut)
    Rectangle(Point(1.5,5.7),Point(2.4,6.3)).draw(donut)

    #Iced Coffee
    iIced = Text(Point(4,6), "Iced Coffee")
    iIced.draw(donut)
    Rectangle(Point(3.5,5.7),Point(4.4,6.3)).draw(donut)

    #--------------------------------------------------------------------------

    #Order button
    order = Text(Point(3,4), "ORDER")
    order.draw(donut)
    Rectangle(Point(2.5,3.7),Point(3.4,4.3)).draw(donut)

    #Quit button
    quit = Text(Point(3,1), "QUIT")
    quit.draw(donut)
    Rectangle(Point(2.5,0.7),Point(3.4,1.3)).draw(donut)

    #Draw donut
    center = Point(3, 2.15)

    #Outer donut
    image1 = Circle(center, 0.65)
    image1.setFill('tan')
    image1.draw(donut)

    #Face of donut
    image2 = Circle(center, 0.5)
    image2.setFill('brown')
    image2.draw(donut)

    #Donut hole
    image3 = Circle(center,0.25)
    image3.setFill('white')
    image3.draw(donut)

    #--------------------------------------------------------------------------

    #Ask for quantities (-,8) for Donuts, (-,5) for Coffees

    #Jelly
    Text(Point(0.7,8), "Quantity:").draw(donut)
    qJelly = Entry(Point(1.2,8),5)
    qJelly.setText("0")
    qJelly.draw(donut)

    #Cream
    Text(Point(1.7,8), "Quantity:").draw(donut)
    qCream = Entry(Point(2.2,8),5)
    qCream.setText("0")
    qCream.draw(donut)

    #Plain
    Text(Point(2.7,8), "Quantity:").draw(donut)
    qPlain = Entry(Point(3.2,8),5)
    qPlain.setText("0")
    qPlain.draw(donut)

    #Sugar
    Text(Point(3.7,8), "Quantity:").draw(donut)
    qSugar = Entry(Point(4.2,8),5)
    qSugar.setText("0")
    qSugar.draw(donut)

    #Chocolate
    Text(Point(4.7,8), "Quantity:").draw(donut)
    qChoc = Entry(Point(5.2,8),5)
    qChoc.setText("0")
    qChoc.draw(donut)

    #Reg Coffee
    Text(Point(1.7,5), "Quantity:").draw(donut)
    qReg = Entry(Point(2.2,5),5)
    qReg.setText("0")
    qReg.draw(donut)

    #Iced Coffee
    Text(Point(3.7,5), "Quantity:").draw(donut)
    qIced = Entry(Point(4.2,5),5)
    qIced.setText("0")
    qIced.draw(donut)



    #Check if order button is clicked
    donut.getMouse()

    #Calculate total
    totalCost = float(0.0)

    #Get jelly input
    getJelly = qJelly.getText()
    tJelly = 1.30 * int(getJelly)

    #Get cream input
    getCream = qCream.getText()
    tCream = 1.30 * int(getCream)

    #Get plain input
    getPlain = qPlain.getText()
    tPlain = .99 * int(getPlain)

    #Get sugar input
    getSugar = qSugar.getText()
    tSugar = .99 * int(getSugar)

    #Get chocolate input
    getChoc = qChoc.getText()
    tChoc = .99 * int(getChoc)

    #Get regular coffee input
    getReg = qReg.getText()
    tReg = 1.75 * int(getReg)

    #Get iced coffee input
    getIced = qIced.getText()
    tIced = 2.25 * int(getIced)

    #Calculate totalCost
    total = tJelly + tCream + tPlain + tSugar + tChoc + tReg + tIced    #price of all items based on quantities
    salesTax = total * .07      # 7% sales tax
    totalCost = total + salesTax


    #Display total/order complete
    Text(Point(3,3), "Order Complete! Your total is: $" + str(totalCost)).draw(donut)


    #Check if quit button is clicked
    donut.getMouse()

    #Exit window
    donut.close()



main()

#--------------------------------------------------------------------------

#def calculateTotal():
