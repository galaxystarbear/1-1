import random
def makelist(k):
    L=[]
    while(True):
        a=random.randint(0,20)
        if(a==0 or len(L)==k):
            return L
        else:
            if a not in L:
                L.append(a)
                
                
n=int(input("Enter the maxium number of possible elements : "))
if(1<=n<=10):
    L1=makelist(n)
    L2=makelist(n)
    print("List1 :",L1)
    print("Liist2 :",L2)
else:
    print("Error")
