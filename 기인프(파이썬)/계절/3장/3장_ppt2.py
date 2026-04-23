s=input("Enter your name and score: ")
print(s,type(s))
name,score=s.split()
print(name,type(name))
print(score,type(score))

name,score,avg=input("Enter your name, age and avg :").split()
score=int(score)
avg=float(avg)
print(name,type(name))
print(score,type(score))
print(avg,type(avg))

name=input("What is your name?")
age=input("How old are you? ")
print("Your name is %s. After 10 years, your age is %d"%(name,int(age)+10))

print("Sogang","University")
print("Sogang","University",sep="***")
print("Sogang","University",sep="")
print("First printing.",end="_")
print("Second printing.",end="")
print("Last printing.")
print("End.")


