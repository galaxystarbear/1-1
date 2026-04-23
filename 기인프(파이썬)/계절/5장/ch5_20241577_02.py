L={}
a=list(input("1. Enter name mid final score : ").split())
a_mid=int(a[1])
a_final=int(a[2])
avg=(a_mid+a_final)/2
L[a[0]]=[a_mid,a_final,avg]
b=list(input("2. Enter name mid final score : ").split())
if b[0] in L:
    print("Already exists!")
else:
    b_mid=int(b[1])
    b_final=int(b[2])
    avg=(b_mid+b_final)/2
    L[b[0]]=[b_mid,b_final,avg]
c=list(input("3. Enter name mid final score : ").split())
if c[0] in L:
    print("Already exists!")
else:
    c_mid=int(c[1])
    c_final=int(c[2])
    avg=(c_mid+c_final)/2
    L[c[0]]=[c_mid,c_final,avg]
print("******************************")
print(L)