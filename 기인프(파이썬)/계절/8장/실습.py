def judint(n):
    if(n.isnumeric()):
        return True
    elif(n[0]=='-' and n[1:].isnumeric()):
        return True
    else:
        return False
    
def judfloat(n):
    if(n.count(".")==1 and n.replace(".","").isnumeric()):
        return True
    elif(n[0]=='-' and n.count(".")==1 and n[1:].replace(".","").isnumeric()):
        return True
    else:
        return False
    
    
L=input("Enter space-seperated data : ").split()
print("Input data :",L)
num=[]
for i in L:
    if(judint(i)):
        i=int(i)
    elif(judfloat(i)):
        i=float(i)
    else:
        continue
    num.append(i)
print("Number data :",num)
