n1,n2,n3=input("Enter").split()
s1,s2,s3=input("Enter").split()
s1=float(s1);s2=float(s2);s3=float(s3)
total=s1+s2+s3
avg=total/3
print("%s : %.2f, %s :%.2f, %s : %.2f"%(n1,s1,n2,s2,n3,s3))
print("Result", "Total score : %.2f"%total,end=" & ",sep="!!!")
print("Average: %.2f"%avg)