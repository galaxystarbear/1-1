L=input("Enter the length of the three sides of the triangle :").split()
a=int(L[0])
b=int(L[1])
c=int(L[2])
if(a**2==b**2+c**2):
    a='Right-angled triange'
elif((b**2==a**2+c**2)):
    a='Right-angled triange'
elif(c**2==a**2+b**2):
    a='Right-angled triange'
else:
    a='No right-angled triangle'
print(a)



data=input("Enter data : ")
if(data.isalpha()):
    print("Only alphabets : %s"%(data))
elif(data.isnumeric()):
    if(int(data)%3==0):
        a=int(data)*10
    else:
        a=int(data)%3
    print("Positive int number : %d"%a)
elif(data[1:].isnumeric() and data[0]=='-'):
    print("Negative int number : %d"%(int(data)*(-10)))
else:
    print("Contain the other character : %s"%data)