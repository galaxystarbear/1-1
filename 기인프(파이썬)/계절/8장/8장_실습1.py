###############################################
import random
L1=[]
L2=[]
while(True):
    i=random.randint(0,10)
    if(i==0):
        break
    elif(i in L1):
        continue
    else:
        L1.append(i)
    if(len(L1)==10): break
    
while(True):
    i=random.randint(0,10)
    if(i==0):
        break
    elif(i in L2):
        continue
    else:
        L2.append(i)
    if(len(L2)==10): break
    
print("List1:",L1)
print("List2:",L2)

###########################################################
n=int(input("Enter positive integer : "))
temp=n
a=0
if(n<=0):
    print("Must be greater than zero")
else:
    while(n>0):
        a +=1
        n=n//10
    print("%d is a %d-digit number"%(temp,a))
######################################################### 
L=[0 for i in range(11)]
num=[]
print("-------- Random number ---------")
for i in range(20):
    i=random.randint(10,20)
    L[i-10] +=1
for i in range(11):
    if(L[i] !=0):
        print("Number %d occurs %d times"%(i+10,L[i]))
    if(L[i]==max(L)):
        num.append(i)
print("The maxium frequency number ***")
for i in num:
    print(i+10,"occurs %d times"%L[i])

###############################################################
S={}
while(True):
    inform=input("Enter data(class name, classroom, number of students) : ").split()
    if(len(inform)==0):
        break
    else:
        if(inform[0] in S):
            print("Already exist!")
        else:
            S[inform[0]]=[inform[1],int(inform[2])]
        
        
for k,v in S.items():
    print("class name : %s, classroom : %s, number of students : %d"%(k,v[0],v[1]))

order=input("Enter two class names to exchange classrooms : ").split()
if(order[0] not in S or order[1] not in S):
    print("No exist class name")
else:
    temp=S[order[0]][0]
    S[order[0]][0]= S[order[1]][0]
    S[order[1]][0]=temp
for k,v in S.items():
    print("class name : %s, classroom : %s, number of students : %d"%(k,v[0],v[1]))

