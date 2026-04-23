import numpy as np
# a=np.array([range(1,10,2), range(2,11,2)])
# a=np.arange(1,11)
# a=a.reshape(2,5)

# a=np.linspace(1,11,6)
# a=np.arange(1,4)
# b=np.array([10,20,30])
# print(b>10)

#list_a=[1,2,3,4,5,6,7,8,9]
#array=np.array(list_a)
#list_b=array.tolist()
#print(type(array))
#print(type(list_b))

# a=np.zeros((2,2)) 
# b=a
# b[0,1]=1
# print(b)
# print(a)

# a=np.zeros((2,2))
# b=a.copy()
# b[0,1]=1
# print(b)
# print(a)


# array = np.arange(8).reshape(2, 4)
# left,right=np.split(array,[1],axis=0)
# print(left)
# print(right)

# V = np.arange(24)
# M = np.arange(24).reshape(6, 4)
# T = np.arange(24).reshape(2,3,4)
#print(T.shape[1])

# array=np.array([7,2,6,7,3,1,1,7,7])
# print(np.where(array==7))

# a = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print(sum(np.einsum('ii->i', a)))

# A = np.arange(20).reshape(5, 4)
# B = np.arange(24).reshape(4, 6)
# print(np.einsum('ij,jk->ik',A,B))
# print(np.einsum('ij->ji',A))
# print(A.T)
# C=np.arange(25).reshape(5,5)
# print(C[C==C.T])

# a=np.ones((16,625))
# print(np.linalg.norm(a))
# print(np.abs(a).sum())

a=np.array([[1,2,3],
           [4,5,6],
           [7,8,9]])

print((a.max(axis=0).mean()))