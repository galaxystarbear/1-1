s="it is good it is bad it is poor"
s1="viviviv"
s2="My score is 89 That's good!"
print(s[len(s)-1])
print(s[:5])
print(s1[::-1]==s1)
news=s2[:12]+input() +s2[14:]
print(news)
s="it is %s I'm %3.0f"%("good",100)
print(s)

find="it"
idx1=s.find(find)
print(idx1)
idx2=s.find(find,idx1+len(find))
print(idx2)
idx3=s.find(find,idx2+len(find))
print(idx3)
idx=s.rfind(find)
print(idx)
idx=s.find("Good")
print(idx)

idx=s.find("it",15,25)
print(idx)
idx=s.rfind("it",0,15)
print(idx)

L=["a","b","D"]
print("".join(L))

s="ABCDEFG"
print(",".join(s))
print(" ".join(s))
print("_".join(s))

L=["David","Lyn","Ann"]
sep=","
s1=sep.join(L)
print(s1,type(s1))

print(s.islower())
print(s.isalpha())
print(s.isalnum())
print(s.isspace())
print(s.isnumeric())
print(s.count("A"))
print(s.find("a"))
print(s.upper())
print(s.lower())

s="Hi everybody!"
s1=s.replace("Hi","Hello")
s2=s.replace("!","")
print(s1)
print(s2)


