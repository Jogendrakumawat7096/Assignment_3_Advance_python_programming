'''Write a Python class named Circle constructed by a radius and two
methods which will compute the area and the perimeter of a circle '''
import math

class Circle:
    def __init__(self,r):
        self.r=r
    def compute_area(self):
        A=math.pi*self.r*self.r
        return A
    def compute_perimeter(self):
        P = 2*math.pi*self.r
        return P
    

circle = Circle(10)
print("Area Of Circle : ",circle.compute_area())
print("perimeter Of Circle : ",circle.compute_perimeter())       
       