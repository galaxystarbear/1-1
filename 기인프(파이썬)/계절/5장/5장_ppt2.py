# classinfo={}
# print("classinfo = ",classinfo)
# classinfo["class1"]=50
# classinfo["class2"]=30
# print("classinfo = ",classinfo)
# classinfo["class3"]=50
# classinfo["class2"]=20
# print("classinfo = ",classinfo)
# num=classinfo["class2"]
# print("std2 is ",num)
# del classinfo["class1"]
# print("classinfo = ",classinfo)

# D1=dict([(1,'a'),(2,'b')])
# D2=dict(({1,'a'},{2,'b'}))
# D3=dict({(1,'a'),(2,'b')})
# print(D1,D2,D3)

# grade={'kim': 89,'park':45,'lee': 78}
# num=grade.get('kim')
# print(num,grade)
# print("##################################")
# num=grade.pop('kim')
# print(num,grade)
# print("#############################")
# grade["kang"]=55
# print(grade)
# print("##################################")
# dictKeyClass=grade.keys()
# print(dictKeyClass,type(dictKeyClass))
# keyL=list(dictKeyClass)
# print(keyL,type(keyL))
# itemL=list(grade.items())

# print(itemL)
# print('kang' in grade)
# print(55 in grade) #key 값에서 찾음


D={'a':1,'b':2,'c':3,'d':4}
print(len(D))
keyList=sorted(D)
print(keyList)
print("####################")
print(D['b'])
print(D.get('b'))
print(D.get('e'))
print(D.get('e',0))
print(D.pop('c'))
print(D)
print(D.pop('c',1))