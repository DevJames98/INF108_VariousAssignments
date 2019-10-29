#import everything from the graphics library
from graphics import *

#Create window
newWin = GraphWin("My Pig", 800, 600)

# Draw Head
center = Point(400, 150)
head = Circle(center, 50)
head.setFill('pink')
head.draw(newWin)

#Draw Eyes
#Eye 1
e1 = Point(380,130)
eye1 = Circle(e1, 10)
eye1.setFill('black')
eye1.draw(newWin)

#Eye 2
e2 = Point(420,130)
eye2 = Circle(e2, 10)
eye2.setFill('black')
eye2.draw(newWin)

#Draw Body
p1 = Point(350,200)
p2 = Point(550,250)
body = Oval(p1,p2)
body.setFill('pink2')
body.draw(newWin)

#Draw Legs
#Leg 1
l1 = Point(400,250)
l2 = Point(425,300)
leg1 = Rectangle(l1,l2)
leg1.setFill('pink4')
leg1.draw(newWin)

#Leg 2
l3 = Point(475,250)
l4 = Point(500,300)
leg1 = Rectangle(l3,l4)
leg1.setFill('pink4')
leg1.draw(newWin)

#Draw Nose
n = Point(400, 170)
nose = Circle(n, 20)
nose.setFill('pink')
nose.draw(newWin)

#Nostril 1
b1 = Point(390,170)
nos1 = Circle(b1, 5)
nos1.setFill('brown')
nos1.draw(newWin)

#Nostril 2
b2 = Point(410,170)
nos2 = Circle(b2, 5)
nos2.setFill('brown')
nos2.draw(newWin)

#Draw Tail
t1 = Point(550,225)
t2 = Point(600, 275)
tail = Line(t1,t2)
tail.setFill('black')
tail.setArrow("last")
tail.draw(newWin)
