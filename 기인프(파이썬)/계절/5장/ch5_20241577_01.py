L1=[15, 12, 8, 6, 11, 18, 1, 10, 16, 2]
L2=[14, 12, 19, 10, 16, 3, 5, 2, 6, 11, 20, 7, 1, 15, 8]
print("List L1 =",L1)
print("List L2 =",L2)
set1=set(L1)
set2=set(L2)
if(len(L1)<=len(L2)):
    set3=set1.difference(set2)
else:
    set3=set2.difference(set1)
if(len(set3)==0):
    print("No Data")
else:
    print("Final List =",list(set3))