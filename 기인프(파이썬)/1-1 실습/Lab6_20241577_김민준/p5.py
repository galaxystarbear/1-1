infile=open("words.txt","r")
total=0
for line in infile:
    line=list(line)
    for i in range(0,len(line)):
        if(("A"<=line[i]) and (line[i]<="Z")):
            total +=1
        elif(("a"<=line[i]) and (line[i]<="z")):
            total+=1

print("파일 안에는 총 {} 개의 알파벳이 있습니다.".format(total))