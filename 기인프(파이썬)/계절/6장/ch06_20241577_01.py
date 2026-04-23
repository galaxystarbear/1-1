S={}
L1=[]
while(True):
    name=input("Enter file name? ")
    if(name==""):
        break
    L=name.split(".")
    if(len(L)==2 and L[0] !="" and L[1] !=""):
        if name in L1:
            print("Warning : Already exist file name")
        else:
            L1.append(name)
            if L[1] in S.keys():
                S[L[1]].append(L[0])
            else:
                S[L[1]]=[L[0],]
    else:
        print("WARNING: Wrong file name")

if(len(S)==0):
    print("No data!")
else:
    print("*** List of file names per extension ***")
    for k,v in S.items():
        v.sort()
        print("%s: %s"%(k,", ".join(v)))
