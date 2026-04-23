L=input().split()
index=0
for data in L:
    if(data.isnumeric() or (data[0]=='-' and data[1:].isnumeric())):
        L[index]=int(data)
        index +=1
    elif(data.count(".")==1 and data.replace(".","").isnumeric()):
        L[index]=float(data)
        index +=1
    elif(data.count(".")==1 and data[0]=='-' and data.replace(".","")[1:].isnumeric()):
        L[index]=float(data)
        index +=1
    else:
        L.pop(index)
print(L)



for j in range(10):
    n=int(input("Enter: "))
    if(n==0): break
    for i in range(1,n+1):
        if(n%i==0): print(i,end=" ")
    print()