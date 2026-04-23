n=input("number :")
if (n.isnumeric() or n[1:].isnumeric()):
    n=int(float(n))
    if(n%2!=0):
        s='odd'
    else:
        s='even'
    print("%d is %s"%(n,s))
elif(n.replace(".","").isnumeric()):
    index_n=int(float(n))
    if(index_n%2!=0):
        s='odd'
    else:
        s='even'
    print("%s is %s"%(n,s))
else:
    print("NOT")
    
name=input("Name:")
if(len(name) !=0):
    print("%s is your name!"%name)
else:
    print("No data")