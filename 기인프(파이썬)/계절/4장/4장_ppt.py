# n=int(input("Enter a number: "))
# if n%2:
#     s="odd"
#     print("%d is %s"%(n,s))
# else:
#     s="even"
#     print("%d is %s"%(n,s))
    
    
    
# x=float(input())
# if not x:
#     print("O")
# else:
#     print("X")
    
# name=input("name :")
# if len(name) !=0:
#     print("yout name is {}".format(name))
# else:
#     print("No data")

        
        
# scores=[67,22,90,0]
# a=[1,2.2,"python",[10,20]]
# L1=[]
# L2=list()
# L3=list("abcd")
# print(L1)
# print(L2)
# print(L3)

# L=[4,1,8,6]
# mL=[1,2.2,"Sogang","대학교",[8,4,"python"]]
# print(len(L),len(mL))
# print(L[0],mL[3],mL[len(mL)-1])
# print(mL[4][2])
# print(mL[4][2][0])

# a=[0,1,2,3,4,5,6,8]
# print(a[6:2])
# print(a[1:7:2])
# print(a[3:20:3])
# print(a[4:4])
# print(a[4:1:1])
# print(a[4:5])
# print(a[4])
# print(a[::-1])


# L=[1,3,5];M=[2,4,6]
# LM=L+M
# print(L,M)
# print(LM)
# L3=L*3
# print(L3)
# print(3 in L, 8 not in M)




L = [10, 20, 10, 20, 10]
L.append(100) 
print(L)
print("************************")
L.insert(2, 100)
print(L)
print("**************************")
data = L.pop()
print(data)
print(L)
print("***************************")
data = L.pop(1)
print(data)
print(L)
print("**********************")
L.remove(10)
print(L)
print("************************")
idx = L.index(10)
c = L.count(10) 
print(idx)
print(c)


L=[]
L.append("first")
L.append("second")
print(L)
print("**************************")
L.clear()
print(L)
print("**************************")
L=list("That's good!")
print(L)
print("**********************")
del L


L=[3,5,1]; M=[2,6,4,10];s="abcd"
L.extend(M)
print(L,M)
L.extend(s)
print(L,s)
print("*********************")
M.sort()
print(M)
print("**************************")
M.sort(reverse=True)
print(M)
print("***********************")
L.reverse()
print(L)

L=[100,900,300,500]
E=enumerate(L)
print(type(E))
EtoL=list(E)
print(EtoL)
L=["Jan","Apr","Sep"]
M=list(enumerate(L))
print(M)

A=["is","are","am"]
C=A
print(id(A),id(C))
C[1]="be"
print(A,C)

L=[1,9,4,2,8]
M=sorted(L,reverse=True)
print("L=",L,",","M=",M)
L.sort()
print("L=",L)
print("########################")
L=[1,9,4]
L1=sorted(L)
L2=L.sort()
print(L1,",",L2,",",L)
print("##############################")
s="Sogang"
L1=sorted(s)
L2=list(s)
L2.sort(reverse=True)
print(L1)
print(L2)
print(s)