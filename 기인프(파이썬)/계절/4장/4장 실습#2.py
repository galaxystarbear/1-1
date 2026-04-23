score=int(input("Enter score :"))
greade="F"
if(score>=90):
    greade="A"
elif(score>=80):
    greade="B"
elif(score>=70):
    greade="C"
elif(score>=60):
    greade="D"
print("Grade is %s"%greade)
    

score = int(input("Enter score :"))
if (score >= 90):
    grade = "A"
else:
    if (score >= 80):
        grade = "B"
    else:
        if( score >= 70):
            grade = "C"
        else:
            if (score >= 60):
                grade = "D"
            else:
                grade = "F"
print("Grade is %s " % grade)
##########################################################

n = int(input("Enter a number: "))
if (n % 2 == 0) and (n % 3 == 0):
    print("%d is divided by both 2 and 3." % n)
elif (n % 2 == 0) and (n % 3 != 0):
    print("%d is divided by 2 but not by 3." % n)
elif (not n % 2 == 0) and (n % 3 == 0):
    print("%d is divided by 3 but not by 2." % n)
else:
    print("%d is neither divided by 2 nor by 3." % n)
    
n = int(input("Enter a number: "))
if (n % 2 == 0):
    if(n % 3 == 0):
        print("%d is divided by both 2 and 3." % n)
    else:
        print("%d is divided by 2 but not by 3." % n)
        
else:
    if(n%3==0):
        print("%d is divided by 3 but not by 2." % n)
    else:
        print("%d is neither divided by 2 nor by 3." % n)