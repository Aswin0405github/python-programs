# a=15
# b=10
# c=20
# max=a
# if b>max:
#     max=b
# elif c>max:
#     max=c
# else:
#     print("all values are equal")
# print(max,"is largest")


# if a>b and a>c:
#     print(a,"is the biggest")
# elif b>a and b>c:
#     print(b,"is the biggest")
# else:
#     print("c is the biggest")

# print("completed")

# i=0
# while i<6:
#     if i==4:
#         i+=1
#         continue
#     print(i)
#     i+=1
# print("thank you")
nums=[7,2,3,1,5,4,6,8,9]
i=0
while i<len(nums):
    if nums[i]==4:
           break
    else:
            print(nums[i])
    i+=1
