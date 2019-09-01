import ptron
import random
from graphics import *

class Dot(object):
    x = 0.0
    y = 0.0
    label = 0

    def __init__(self):
        self.x = random.randint(1, 400)
        self.y = random.randint(1, 400)
        if (self.x > self.y):
            self.label = 1
        else:
            self.label = -1
    def show(self): #returns a circle with color
        c = Circle(Point(self.x,self.y),5)
 #       if self.label == 1:
 #           c.setFill("green")
 #       else:
 #           c.setFill("red")
        return c

def setup():
    win = GraphWin("Perceptron", 400, 400)
    win.setBackground("light gray")
    line = Line(Point(0,0),Point(400,400))
    line.draw(win)
    p = ptron.perceptron()
    inputs = [-1, 0.5]
    guess = p.guess(inputs)
   
    return win
def main():
    win = setup()
    points = []
    for i in range(100):
        point = Dot()
        points.append(point)
        

    for i in points:
        inputs = [i.x,i.y]
        target = i.label
        p = ptron.perceptron()

        p.train(inputs, target)
        guess = p.guess(inputs)     
        c = Dot.show(i)
        if guess == target:           
            c.setFill("green")
        else:
            c.setFill("red")
            print(guess," ",target)
        c.draw(win)
    
    
main()

