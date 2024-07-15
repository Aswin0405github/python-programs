import numpy as np

# a=np.array([1,2,3])
# # print(a)
# # print(type(a))
# a=np.array([[1,2,3,4,5,6,7],[11,12,13,14,15,16,17],
#             [110,120,130,140,150,160,170],[101,102,103,104,105,106,107]])
# # print(a)
# print(a.ndim)
# print(a.shape)
# print(a.itemsize)
# print(a.size)
# print(a.nbytes)
# print(a[1])
# print(a[1,2])
# print(a[0:])
# print(a[0:3])

# a=np.array([[1,2,3],[4,5,6]],[[5,6,7],[10,11,12]])
# # print(a.ndim)
# # print(a[0,0:,1:])

# print(np.zeros(5))
# print(np.zeros((2,3)))
# print(np.zeros((2,2,3)))

# print(np.ones(5))
# print(np.ones((2,3)))
# print(np.ones((2,2,3)))
# print(np.full((2,3,3),88)) 
# print(np.full_like(a,5))
# print(np.random.randint(1,9,size=(4,3)))
# print(np.random.randint(9,size=(4,3)))
# print(np.identity(5))


# on

# a=np.array([1,2,3,4])
# print(a)

# b=a
# b[1]=100
# print(b)
# print(a)

# b=a.copy()
# b[1]=200
 # print(a,b)
# l=[1,2,3]
# print(l*2)
# print(a*2)
# print(a+2)
# print(a-2)
# print(np.cos(a))
# print(np.matmul(a,b))
# print(np.linalg.det(a))



# a=np.array([[1,2,3],[4,5,6]])
# print(a)
# print(np.min(a))
# print(np.max(a))
# print(np.mean(a))
# print(np.median(a))

# after=a.reshape(8,1)
# print(after)
# after=a.reshape(4,2)
# print(after)
# after=a.reshape(2,2,2)
# print(after)

# a=np.array([1,2,3,4])
# b=np.array([5,6,7,8])
# print(np.hstack([a,b]))
# print(np.vstack([a,b]))
# print(np.arange(1,10,2))
# print(np.arange(5))
# print(np.arange(12).reshape(4,3))
# print(np.linspace(1,5,10))
# a=np.array([[1,2,3,4],[5,6,7,8]])
# print(a.ravel())