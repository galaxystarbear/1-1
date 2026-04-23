fr=open("in.txt","r")
fp=open("out.txt","w")
s=fr.read()
fp.write(s)
for i in fr:
    print(i,end="",file=fp)
for i in range(2):
    s=fr.readline()
    print(s)
for i in fr:
    fp.write(i) 
fp.close()
fr.close()


fp_r=open("in_mul.txt",'r')
fp_w=open("out_mul.txt",'w')
print("THe square results are", file=fp_w)

for i in fp_r:
    num=list(int(x) for x in i.split())
    print(num)
    for j in range(len(num)):
        sq=num[j]**2
        print("%4d "%sq, file=fp_w,end="")
    fp_w.write("\n")
    
fp_r.close();fp_w.close()
