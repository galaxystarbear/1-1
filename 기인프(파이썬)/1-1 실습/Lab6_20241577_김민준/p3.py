import random
r= random.randint(1,10)
while True:
    n=input("숫자를 맞춰보세요 ( 1~10 ):")
    n=int(n)
    if(n<r): print("정답은 {}보다 큽니다.".format(n))
    elif(n>r): print("정답은 {}보다 작습니다.".format(n))
    else:
        print("정답입니다. 입력한 숫자는 {}입니다.".format(n))
        break
print("종료합니다.")
