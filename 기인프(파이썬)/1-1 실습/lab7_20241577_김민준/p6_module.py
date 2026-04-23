def getNumber():
    import random
    a=random.randint(1,45)
    return a
import math
p = math.pi
class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    
    def calcPerimeter(self):
        return 2*p*self.radius
    def calcArea(self):
        return p*self.radius*self.radius
    