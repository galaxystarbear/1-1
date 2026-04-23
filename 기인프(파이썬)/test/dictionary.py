contacts = {'Kim':'010-123-4567',
'Park':'010-123-4568',
'Lee':'010-123-4569' }
# contacts= ['kim','lol']
#있는지 확인
# while True:
#     n=str(input("name:"))
#     if(contacts.get(n)==None):
#         print("fail")
#     else:
#         print("success")
#         break


# key값 바꾸기
# contacts['Kim']="1234"
# print(contacts)


#리스트로 바꾸기
# print(contacts.items())
# a=list(contacts.items())
# print(a)
# print(a[0][1])

# for k in contacts.keys():
#     print(k)
#     print(contacts[k])

# # for v in contacts.values():
# #     print(v)

# for k,v in contacts.items():
#     print(k)
#     print(v)

# while True:
#     n=str(input("name:"))
#     if n not in contacts:
#         print("zz")
#         break
#     else:
#         print(contacts[n])