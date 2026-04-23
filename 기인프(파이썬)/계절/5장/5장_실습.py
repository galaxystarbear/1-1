# print("1. 정수 데이터 1개를 입력 받아서 튜플에 저장/출력하기")
# n=int(input("Enter int num: "))
# T=n,
# print("tuple T =",T)

# print("2. 튜플 T를 집합 S으로 변환/출력하기")
# S=set(T)
# print("set S=",S)

# print("3. 집합 S에 리스트 L=[4,5,4,7,8,4]의 원소를 추가/출력하기")
# L=[4,5,4,7,8,4]
# S.update(set(L))
# print("set S=",S)

# print("4. 문장 입력 받기")
# n=input("Enter sentence: ").split()
# print("Sentences entered consists of %d words"%len(n))

# print("5. 입력 받은 문장에서 중복 단어 삭제/오름차순으로 단어 출력하기")
# sentence=list(set(n))
# sentence.sort()
# print("Final sentence:"," ".join(sentence))




# L=input().split()
# a=int(input("Enter index: "))
# if(-1<a<len(L)):
#     if(L[a].isnumeric() or (L[a][1:].isnumeric() and L[a][0]=="-")):
#         L[a]=int(L[a])
        
#     elif(L[a].count('.') ==1):
#         if(L[a][0]=="-"):
#             n=L[a].replace(".","")
#             if(n[1:].isnumeric()):
#                 L[a]=float(L[a])
#             else:
#                 L.pop(a)     
#         else:
#             n=L[a].replace(".","")
#             if(n.isnumeric()):
#                 L[a]=float(L[a])
#             else:
#                 L.pop(a)    
#     else:
#         L.pop(a)   
# else:
#     print("Error") 
    

# print("L=",L)

L=input().split()
a=int(input())
if(-1<a<len(L)):
    if(L[a].isnumeric() or (L[a][0]=="-" and L[a][1:].isnumeric())):
        L[a]=int(L[a])
    elif(L[a].count(".")==1 and L[a].replace(".","").isnumeric()):
        L[a]=float(L[a])
    elif(L[a][0]=="-" and L[a].count(".")==1 and L[a][1:].replace(".","").isnumeric()):
        L[a]=float(L[a])
    else:
        L.pop(a)
else:
    print("Error")
print("L=",L)