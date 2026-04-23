import random

def getNumber():
    a=random.randint(1,45)
    return a

L=[]
while True:
    a=getNumber()
    if(L.count(a)==0): L.append(a)
    if(len(L)==6): break
L.sort()
print("**로또 추첨을 시작합니다.**")
print("추첨된 로또 번호==> ",end="")
for i in range(6):
    print(L[i],end=" ")
