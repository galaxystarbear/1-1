import random
def detprime(N):
    k=True
    for i in range(2,N):
        if(N%i==0):
            k=False
            break
    return k

L=[]
while(True):
    a=random.randint(2,100)
    if  a not in L:
        if(detprime(a)):
            print("%d is prime number"%a)
        else:
            print("%d is not prime number"%a)
        L.append(a)
    else:
        break
        