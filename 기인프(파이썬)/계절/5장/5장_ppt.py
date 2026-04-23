# T=()
# T1=(10,)
# T2=10,
# print(T1,type(T1))
# print(T2,type(T2))
# s=(10)
# print(s,type(s))

# T3="David", 20, "CS"
# print("T3=",T3)
# name,age,major=T3
# print("name =%s, age=%d, major=%s"%(name,age,major))
# T4=tuple("abc")
# T5=("ABC",)
# T6=("ABC")
# print(f"T4={T4}, T5={T5}, T6={T6}")
# T=T4+T5
# print("T=",T)
# del T

# x=23;y=-23
# print("x=%d,y= %d"%(x,y))
# x,y=y,x
# print("x=%d,y= %d"%(x,y))


# T=(1,[20,30],[],"sogang")
# T[1][1]=40
# T[2].append([100,200])
# print("T=",T)
#T[1]=["abc",20] 오류 발생


S1=set()
S2=set([10,3,"abc",4,10])
S3=set("Good!! ^^")
print(S1)
print(S2)
print(S3)
S2.add("abc")
S2.add("def")
S2.update([10,20,30])
print(S2)
S2.remove(30)
print(S2)
S2.discard(30)
print(S2)
n=S2.pop()
print(n)
print(S2)
S2.clear()
print(S2)


L=[1,1,2,2];B={3,4,5,6}
A=set(L)
print(A)
A=A.union({3,4})
print(A)
C=A|B
D=A&B
E=A.difference(B)
print(C)
print(D)
print(E)
#S={10,20,[100,200]} 집합 원소로 리스트는 안됨!!

