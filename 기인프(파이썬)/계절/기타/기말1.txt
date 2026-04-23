import random
def det(L):
    L1=[]
    for data in L:
        if(data.isnumeric() or (data[1:].isnumeric() and data[0]=='-')):
            L1.append(int(data))
        elif(data.count('.')==1):
            temp=data.replace(".","")
            if(temp[0]=='-' and temp[1:].isnumeric()):
                L1.append(int(float(data)))
            elif(temp.isnumeric()):
                L1.append(int(float(data)))
    return L1

L=input("Enter data : ").split()
L1=[]
L2=[]
if(L==[]): print("WARNING : No Data!")
else:
    final=det(L)
    if(final==[]):
        print("WARNING : No Data!")
    else:
        print("Final data list :",final)
        a=random.choices(final,k=2)
        if(a[0]<1 or a[1] <1):
            print("WARNING : Number %d or %d is not greater than 1"%(a[0],a[1]))
        else:
            for i in range(1,min(a)+1):
                if(a[0]%i==0 and a[1]%i==0):
                    L2.append(i)
            if(L2==[]):
                print("WARNING:No Data!")
            else:
                print("Common divisor of %d and %d : "%(a[0],a[1]),end="")
                for i in range(len(L2)-1):
                    print(L2[i],end=', ')
                print(L2[-1])

