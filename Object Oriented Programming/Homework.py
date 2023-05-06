#Problem 1
#Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
class Line(object):

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print(li.distance())
print(li.slope())

#Problem 2
#Fill in the class


class Cylinder:

    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.radius = radius
        self.height = height


    def volume(self):
        volume = self.height*self.pi*self.radius**2
        print(format(volume))


    def surface_area(self):
        area = (2*self.pi*self.radius**2) + (2*self.pi*self.radius*self.height)
        print(format(area))



# EXAMPLE OUTPUT
c = Cylinder(2, 3)
c.volume()
c.surface_area()
