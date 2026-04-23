from p6_module import *
r1=getNumber()
r2=getNumber()

n1=Circle(r1)
n2=Circle(r1)
l1=n1.calcPerimeter()
l2=n2.calcPerimeter()
s1=n1.calcArea()
s2=n2.calcArea()

print("반지름이 각 각 {},{}인 두 원의 둘레의 합은 {}, 넓이의 합은 {}입니다.".format(r1,r2,(l1+l2),(s1+s2)))