# sub=["I","you"]
# ver=["play","Love"]
# obj=["hockey","football"]
# for i in sub:
#     for j in ver:
#         for k in obj:
#             print(i+" "+j+" "+k)


# l=[]
# a=int(input("Enter the number of numbers"))   
# i=0 
# s=0
# while i<a:
#     k=int(input("Enter number"))
#     l.append(k)
#     s+=k
#     i+=1
# print(l,s)


##########################################

#with thegiven list[12,24,35,25,88,120,155,88,120,155]
# t=[12,24,35,24,88,120,155,88,120,155]
# temp=[]
# for i in t:
#     if i not in temp:
#         temp.append(i)
# print(temp)


# s=input("enter a sentance:")
# u=l=0
# for i in s:
#     if i.isupper():
#         u+=1
#     elif i.islower():
#         l+=1

# print("number of upper case:",u)
# print("number of lowercase:",l)
# v=[2,3,4,5]


# i=len(v)-1


# def sum(v,i):
   
#     if i ==0:
#         return v[0] 
#     else:
#         return v[i]+sum(v,i-1)
# print(sum(v,i))

    
# def sum(val):
#     if len(val)==1:
#         return val[0]

#     else:
#         return val[0]+sum(val[1:])

        
 
# def sum(val):
#     if len(val)==1:
#         return val[0]
#     else:
#         return val[0]+sum(val[1:])



# val=[1,2,[3,4],[5,6]]

# def issum(data):
#     for i in data:
#         t=0
#         if type(i)==type([]):
#             t+=issum(i)
#         else:
#             t+=i
#         return t

# a=[1,2,3,4]
# b=[10,1,6]
# print([i+j for i in a for j in b])     

# a=[1,2,3,4]
# b=[1,2,3,4]

# print(list(map(lambda i,j:i+j,a,b)))  

# num=[1.2,2.3,3.4]
# print([int(i) for i in num])
# 

# mat=[[1,2],[3,4],[5,6],[7,8]]

# print([[j[i] for j in mat] for i in range(len(mat[0]))])


# i=int(input("ent num:"))
# t=0
# while i>0:
#     t=(t*10)+(i%10)
#     i=i//10
# print(t)

# l=[12,75,150,180,145,525,50]
# for i in l:
#     if i%5==0:
#         if i==150: 
#             pass
#         elif i>500:
#             break
#         else:
#             print(i,end=" ")


 
# l=["tool",23,3.4,"bar",55,"toolbar"]
# print([i for i in l if str(i).isalpha()])