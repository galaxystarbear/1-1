std1,std2,std3=input("Enter the names and scores of 3 students seperated by /:").split("/")
std1_name,std1_score=std1.split()
std2_name,std2_score=std2.split()
std3_name,std3_score=std3.split()
sum=int(std1_score)+int(std2_score)+int(std3_score)
avg=sum/3
print('"Student1 name : %s, score : %d"'%(std1_name,int(std1_score)))
print('"Student2 name : %s, score : %d"'%(std2_name,int(std2_score)))
print('"Student3 name : %s, score : %d"'%(std3_name,int(std3_score)))
print('"Total score : %d, Average : %.2f"'%(sum,avg))


# std=input("Enter the names and scores of 3 students seperated by /:").split("/")
# L=[s.split() for s in std]
# sum=0
# for index,inform in enumerate(L):
#     print(f"std{index} name : {inform[0]}, score : {inform[1]}")
#     sum +=int(inform[1])

# print('"Total score : %d, Average : %.2f"'%(sum,sum/3))   