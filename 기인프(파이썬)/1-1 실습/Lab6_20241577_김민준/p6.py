infile=open("data.txt","r")
fw=open("output.txt","w")
s=infile.readlines()

total=0
for i in s:
    i=i.split()
    a=float(i[0])
    print(a)
    total += a
w=(total/len(s))
print(w,total)
fw.write("합계={}\n".format(total))
fw.write("평균={}\n".format(w))
fw.close