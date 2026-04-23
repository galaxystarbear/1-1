total=0
while True:
    n=input("정수를 입력하시오:")
    n=int(n)
    if(n==0):break

    total +=n
print("합은 {} 입니다.".format(total))    