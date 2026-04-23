import math
p=math.pi

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def calcPerimeter(self,n):
        return 2*p*n
    def calcArea(self,n):
        return p*n*n
    
a=Circle(100)
r=a.radius
s=a.calcPerimeter(r)
k=a.calcArea(r)
print("반지름:{} 원의 면적: {} 원의 둘레: {}".format(r,k,s))