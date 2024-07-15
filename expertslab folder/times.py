import time


# print(time.time())
# print(time.localtime(time.time()))


# print(time.asctime())


import timeit

# print(timeit.timeit('[x*x for x in range(5)]'))
# def func(x):
#     print(x)
# a=12

# print(timeit.timeit(lambda :func(a),setup="pass",number=1))

# value="import value"
# code='''
# def call():
#     return random.randint(10,50)'''
# print(timeit.timeit(code,setup=value))

import datetime
# print(datetime.date(2023,6,22))

# dt=datetime.date.today()
# print(dt.weekday())
# print(dt.isoweekday())
# print(dt.isocalendar()) 

# print(time.tzname())
# print(time.timezone())
# # print(time.tzname[time.daylight])
# # print(datetime.datetime.now().astimezone().tzname())

# # print(datetime.datetime.now())
# tup=(2025,5,12,5,15,25,0,0,0
#      )
# print(time.mktime(tup))



# random
import random
# print(random.random())
# print(random.uniform(1,10))
# print(random.randint(1,10))


# v=[1,2,3,4,5,5,6,6,6,6,5,4,5,6,6,6,4,'e',5,6,6]
# print(random.choices(v,k=3))

# v=["a","b","c","d","e"]
# print(random.choices(v,weights=[1,2,3,4,5],k=3))

# print(random.choice(v))

# print(random.shuffle(v))
# print(random.sample(v,k=4))

#######################################################

# from time import sleep
# import random
# lt=[]
# print("creating 100 tickets!")
# for i in range(100):
#     lt.append(random.randrange(10000,100000))
# v=random.sample(lt,k=2)
# print("Finding winners!!...Please wait!!")
# sleep(5)
# print(f"The winners are {v}")

########################################################

# print(__name__)


########################################################


# x=isinstance(5,dict)
# x=isinstance(5,int)
# x=isinstance((5),tuple)
# x=isinstance({5},(float,int,set,dict))
# print(x)


########################################################

#any
#all

# a=[False,False,True]
# b=[True,True,True]

# a=[1,1,0]
# b=[0,0,0]

# a=['aswin',"","pp",1]
# b=["","",""]

# # print(any(a))
# # print(all(a))
# # print(any(b))
# # print(any(a))

##############################

#abs()

# a=-11
# a=11.7
# print(abs(a))

############################################

#round min max

# print(min(12,0,-3,4,67,-6))
# print(max(12,0,-3,4,67,-76))

import math
# print(math.sqrt(3))


# print(math.ceil(5.66))
# print(math.floor(6.008))
# a,b=math.modf(10.23 )
# print(a,b)

# import statistics
# help
# (statistics)


# import statistics as s
# print(s.mean([1,2,3,4,5]))
# print(s.median([1,2,3,4,5,6]))
# print(s.mode([1,2,3,3,4,5,6,6,6]))
# print(s.multimode([1,2,1,6,6]))

