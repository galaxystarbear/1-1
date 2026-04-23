
a=input("First numeric code :")
b=input("Second numeric code :")

if(not a.isnumeric() or not b.isnumeric()):
    print("Waring: No positive int number( > 0)")
elif((len(a)<=2) or (len(b) <=2)):
        print("Input data must be greater than 2 characters!")
else:
    a1=list(a);b1=list(b)    
    a1.sort();b1.sort()
    a1.pop();a1.pop(0)
    b1.pop();b1.pop(0)
    if(a1==b1):
        print("%s, %s : Perfect code!"%(a,b))
    else:
        print("%s, %s : Not perfect code!"%(a,b))