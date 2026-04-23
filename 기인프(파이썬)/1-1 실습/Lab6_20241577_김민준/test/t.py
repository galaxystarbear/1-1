
infile = open("words.txt","r")
count = 0
for line in infile: 
    for i in line:
        if (i >= "a" and i <= "z") or (i <= "Z" and i >= "A"):
            count += 1
print("파일 안에는 총 {}개의 알파벳이 있습니다.".format(count))
infile.close()