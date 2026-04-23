foods = { "떡볶이" : "오뎅",
"짜장면" : "단무지",
"라면" : "김치",
"피자" : "피클",
"맥주" : "땅콩",
"치킨" : "치킨무",
"삼겹살" : "상추" }

while True:
    k=str(list(foods.keys()))
    n=input("['떡볶이','짜장면','라면','피자','맥주','치킨','삼겹살'] 중 좋아하는 것은?")
    n=str(n)
    
    if(n=="끝"): break
    elif(n in k):
        print("<{}> 궁합 음식은 <{}>입니다.".format(n,foods[n]))
    else:
        print("그런 음식이 없네요")
        continue
    
