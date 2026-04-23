L=[27,19,43,28,1]
print("L=",L)
print("1. Sort the elements in list L descending order")
L.sort(reverse=True)
print("L=",L)
print("2. After deleting the last element in list L, print out the deleted data")
data=L.pop()
print("Deleted data is", data)
print("L=",L)
print("3. Add the deleted data as the first element in list L")
L.insert(0,data)
print("L=",L)
print("4. Receive the indedx number of list L and delete the element at that location if it is a valid index value")
idx=int(input("Enter index num : "))
if(0<=idx<len(L)):
    L.pop(idx)
else:
    print("Error")
print("L=",L)
print("5. Add the entered data to the end of list L")
data=input("Enter any type data :")
L.append(data)
print("L=",L)
print("6. Print out whether the recieved data exists in list L")
data=input("Enter data to find :")
if data in L:
    print("Found!")
else:
    print("No found!")