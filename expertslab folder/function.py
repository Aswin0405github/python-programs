# def call():
#     a=[]
#     b=[1,2,3,4,5]
#     for i in b:
#         a.append(i+1)
#     print(a)
# call()
# print(a)

# def add(a,b):
#     sum=a+b
#     print(sum)

# add(2,3)
# add(5,6)
# add(6,7)

# def avg(n):
#     s=0
#     for i in range(n):
#         a=int(input("enter number to find value:"))
#         s+=a
#     print("Average:",s/n)
# a=int(input("enter the number of values:"))
# avg(a)


# lambda
# a=lambda a,b,c:a+b/c
# print(a(2,3,4))

# a=lambda x,y:x if x>y  else y
# print(a(1,2))

# s=['d',"de","dev","devin","abin"]
# s.sort()
# s.sort(key=lambda s:len(s))
# print(s)

# def func(v=2):
#     c=v*2
#     return c

# x=2
# high= lambda x,func:x+func
# print(high(3,func()))


# composition


# def add(x):
#     return x+2

# def mul(x):
#     return x*2
# print("result:",mul(add(5)))

# enumarate

# val=["red","black","green"]
# for i in val:
#     print(i," ",val.index(i),end="  ")

# for i,j in enumerate(val):
#     print(i,j)
# for j in enumerate(val):
#     print(j)

# map function 
# def sqr(a):
#    return a*a
# val=[2,3,4,5 ]
# print(map(sqr,val))
# print(list(map(sqr,val)))


# print(list(map(lambda a:a*a,[2,3,4,5])))

# a=[1,2,3,4]
# b=[5,6,7,8]
# c=[10,11,12,13]
# print(list(map(lambda a,b,c:a+b+c,a,b,c)))

# print(list(filter(lambda i:i%3,range(1,11))))


# reduce function (function tools)

# import functools as fun
# val=[1,2,3,4]
# print(fun.reduce(lambda x,y:x+y,val))

# s="devin 123"
# l=[int(i) for i in s if i.isdigit()]
# print(l)
# s="a citizen of ekm fought and won the election"
# w=["in","of","a","and","the"]
# a=s.split()
# for i in a:
#     if i in w:
#         a.remove(i)

# print(" ".join(a))


# value=[[1,2,3],[4,5,6],["a","b"]]
# l=[i[0] for i in value]
# print(l)