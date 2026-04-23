L=[3,1,0,26,-2,19,9,-88]
print("L=",L)
a,b=input("Enter two index number of list of L: ").split()
a=int(a);b=int(b)
if(-1<a<len(L) and -1<b<len(L)):
    c=input("Enter operater symbol(+,*,-,/) : ")
    if(c=="+"):
        data=L[a]+L[b]
        L.append(data)
    elif(c=="*"):
        data=L[a]*L[b]
        L.append(data)
    elif(c=="-"):
        data=L[a]-L[b]
        L.append(data)
    elif(c=="/"):
        if(L[b]==0): print("Cannot divide by zero")
        else:
            data=L[a]/L[b]
            if(int(data) != data and data <0): data=int(data)
            L.append(int(data))
    else:
        print("%s is unsuppoerted operater"%c)
else:
    print("Error : list index out of range")
    
print("Final List = ",L)
