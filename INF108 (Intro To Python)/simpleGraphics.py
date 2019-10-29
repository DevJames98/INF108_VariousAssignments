# simple graphics programming
from graphics import * #import everything from the graphics library
newWin = GraphWin('Shapes')
# draw a circle
center = Point(100, 100)
redCircle = Circle(center, 30)
redCircle.setFill('red')
redCircle.draw(newWin)
# open a new window 200x200 pixels
# draw a line
aLine = Line(Point(20,20), Point(20,100))
aLine.draw(newWin)
# draw a rectangle
aRectangle = Rectangle(Point(100,20), Point(150,100))
aRectangle.draw(newWin)
newWin.getMouse() # pause for click in window newWin.close() #close/destroy the window
newWin.close()
