S1={}
S2={}
L=[]
L1=[]
temp=1
while(True):
    a=input("Enter student data(name score1 score2): ").split()
    if(len(a)==0):
        break
    elif(len(a) !=3):
        print("WARNING : number of data entered must be 3")
        continue
    else:
        name=a[0]
        score1=int(a[1])
        score2=int(a[2])
        S1[name]=int((score1+score2)/2)
        L.append(int((score1+score2)/2))
print("***********************************")
print()
if(S1=={}):
   print("No Input Data!")
else:
    data=input("Enter student name you want to know rank : ")
    L=list(set(L))
    L.sort(reverse=True)
    for i in range(len(L)):
        a=temp
        for k,v in S1.items():
            if(L[i]==v):
                S2[k]=a
                temp +=1
    if(data in S1):
        print("The rank of %s is %d"%(data,S2[data]))
    else:
        print("WARNING : No exists name")
    data2=int(input("Enter rank to know who : "))
    for k,v in S2.items():
        if(data2==v):
            L1.append(k)
    if(L1==[]):
        print("There is no student of %d rank"%data2)
    else:
        print("The rank of %s is %d"%(",".join(L1),data2))
        
        
    
