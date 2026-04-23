# for name in ["Ann","jim","Yoon","Dan"]:
#     print("Hi",end=" ")
#     print(name)
    
# L=[10,20,30,40]
# for num in L:
#     print(num,end=" ")
# print()
# print(L)

# for num in L:
#     result=num*num
#     print(result,end=" ")
# print()
# print(L)

# for i,num in enumerate(L):
#     L[i]=num*num
#     print(L[i],end=" ")
# print()
# print(L)



# s=input()
# vowels="aeiouAEIOU"
# reuslt=""
# for c in s:
#     if c not in vowels:
#         reuslt +=c
# print(reuslt)


# vowels=0;conosonants=0
# for c in s:
#     if c.isalpha():
#         if c in "aeiouAEIOU":
#             vowels +=1
#         else:
#             conosonants +=1
# print(vowels)
# print(conosonants)

# L=[1,3,6]
# for i in range(len(L)):
#     L[i]=L[i]**2
# print(L)
# print("######################")
# S="abcdef"
# for j in range(len(S)-1,-1,-1):
#     print(S[j],end="")
# print("##########################")
# for i in range(3):
#     print("range() test")
    
# a=[1,2,3,4]
# result=[]
# for num in a:
#     result.append(num*3)
# print(result)
# result=[num*3 for num in a]
# a=list(range(1,21,2))
# result=[num*10 for num in a if num%3==0]
# print(result)
# L=["apple","banana","pear"]
# L1=[s.upper() for s in L if s[0]=='a']
# print(L1)


# D={"a":[10,20],"b":[30,40]}
# for data in D.items():
#     print(data[0])
#     print(data[1][0])
#     print(data[1][1])
# print()
# for key,val in D.items():
#     print(key)
#     print(val[0])
#     print(val[1])
# print()
# for key in D.keys():
#     print(key)
#     print(D[key][0])
#     print(D[key][1])
# print()
# for key in D:
#     print(key)
#     print(D[key][0])
#     print(D[key][1])

# a=[int(x) for x in input().split() if x.isnumeric()]
# for i in a:
#     if(i%3==0) or (i%4==0):
#         continue
#     print(i,end=" ")
# print()

n=int(input("Prime? : "))
prime=True
for i in (2,n**0.5):
    if n%i==0:
        prime=False
        break
if(prime): print("O")
else: print("X")