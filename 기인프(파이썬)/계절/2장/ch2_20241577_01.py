num=1002
a1=num//1000
a2=num%1000//100
a3=num%100//10
a4=num%10
sum=a1+a2+a3+a4
print("Number",num,":",a1,'+',a2,'+',a3,'+',a4,'=',sum)
print("Average :",sum/4)