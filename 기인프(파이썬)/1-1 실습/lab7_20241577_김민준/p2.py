def add(a,b):
    return a+b
def m(a,b):
    return a-b
def multi(a,b):
    return a*b
def s(a,b):
    return a/b

a= 20
b=10
print("({}+{})={}".format(a,b,add(a,b)))
print("({}-{})={}".format(a,b,m(a,b)))
print("({}*{})={}".format(a,b,multi(a,b)))
print("({}/{})={}".format(a,b,s(a,b)))