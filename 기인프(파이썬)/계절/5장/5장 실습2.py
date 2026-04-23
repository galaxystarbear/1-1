print("1. 빈 사전 D 생성/출력하기")
D={}
print(D)
print("2. 빈 사전에 D에 아래와 같은 원소 추가/출력하기")
D['1반']=[60,'D104']
D['2반']=[90,'D105']
D['3반']=[30,'D104']
print(D)
print("3. 사전 D의 키 값들을 리스트에 저장/출력하기")
key_L=list(D.keys())
print("key_L =",key_L)
print("4. 사전 D의 (key,value) 값들을 리스트에 저장/출력하기")
data_L=list(D.items())
print("data_L =",data_L)
print('5. 반명을 입력받아서 해당 반의 수강생 수와 강의실 정보 출력하기 \n   입력받은 반이 존재하지 않을 때는 "Not exist"출력하기')
a=input("Enter class name : ")
if a in D:
    print(f"{a}의 수강생 수는 {D[a][0]}명이고 강의실은 {D[a][1]}입니다.")
    D[a][0] +=10
    print(f"After increase of 10 students of {a}, D={D}")
else:
    print("Not exist")