from p3_module import *
n=input("사칙연산 식을 입력하시오:")
n1,n2,n3=n.split()
n1=int(n1)
n3=int(n3)

if(n2=="+"):
    print(n,"=",add(n1,n3))    
elif(n2=="-"):
    print(n,"=",m(n1,n3))
elif(n2=="*"):
    print(n,"=",multi(n1,n3))
elif(n2=="/"):
    print(n,"=",div(n1,n3))
