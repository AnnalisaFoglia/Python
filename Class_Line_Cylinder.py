#calculating distance and slope of a line
class Line:

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        #unpacking the tuples
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)
coordinate1=(4,3)
coordinate2=(7,9)
li= Line(coordinate1, coordinate2)
print (li.distance())
print (li.slope())

#calculating volume and area of a cylinder
from math import pi

class Cylinder:

    def __init__(self, height=1, radius=1):#set default values to 1
        self.height=height
        self.radius=radius

    def volume(self):
        return self.height*pi*(self.radius)**2

    def area(self):
        return (2*pi*self.radius*self.height)+(2*(pi*(self.radius)**2))

c=Cylinder (5, 7)
print (c.volume())
print (c.area())
