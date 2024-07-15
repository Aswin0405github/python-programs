# class employee:
#     pass

# emp1=employee()
# emp2=employee()


# print(emp1)
# print(emp2)

# class employee:
#     pass

# emp1=employee()
# emp2= employee()

# emp1.first='devin'
# emp1.last='mathew'
# emp1.mail='devin@gmail.com'
# emp1.pay=10000

# emp2.first='dainty'
# emp2.last='mathew'
# emp2.mail='dainty@gmail.com'
# emp2.pay=20000


# class employee:
#     "this is class employee"
#     rais=1.04
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.mail=first+last
#         self.pay=pay
#     def fullname(self):
#         return f"{self.first} {self.last}"  
#     def raiseamt(self):
#         return self.pay*self.rais

# emp1=employee('devin','mathew',1000)
# emp2=employee('dainty','mathew',2000)

# # print(emp1.fullname())
# # print(emp2.fullname())

# # print(emp2.raiseamt())
# print(employee.__doc__)


# ##############

# def tags(tag):
#     def text(msg):
#         print(f"{tag} {msg} {tag} s")
#     return text
# a=tags("B")
# a("oo")



# def decorator_function(orginal):
#     def wrapperfunction(*args,**kwargs):
#         print(f"wrapper executed before {orginal.__name__}")
#         return orginal(*args,**kwargs)
#     return wrapperfunction


# # @decorator_function
# # def display():
# #     print("display func")

# # display()

# @decorator_function
# def info(name,age):
#     print(f"ran with argument {name} {age}")

# info("aswin","18")

###########################################

# class decorator_class:
#     def __init__(self,orginal_fun):
#         self.orginal_fun=orginal_fun
#     def __call__(self,*args,**kwargs):
#         print(f"method will execute before {self.orginal_fun.__name__}")
#         return self.orginal_fun(*args,**kwargs)
# @decorator_class
# def display():
#     print("display function")

# display()
 
# def timetaken():
#     import time
#     s=time.time()
#     l=[]
#     for i in range(1,10001):
#         l.append(i**2)
#     i=time.time()
#     print((s-i)*1000)

# timetaken()

# import time
# def find_time(func):
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         calctime=func(*args,**kwargs)
#         stop=time.time()
#         print(func.__name__+"took:  "+str((stop-start)*1000)+"  mile sec")
#         return calctime
#     return wrapper

# @find_time
# def calc_timersqr(numbers):
#     ls=[]
#     for i in numbers:
#         ls.append(i*i)
#     return ls

# array=range(1,10000)
# res=calc_timersqr(array)
# print(res)

# ##########################


# from typing import Any


# class sample:
#     value="hi,i am class variable"
#     def __init__(self) :
#         print("hello")

#     def call(self):
#         value="i am local variable "
#         print(self.value)
    
    
       


# new=sample()
# new.call()
# new.value="updated value"
# new.call()
# # print() 
# # newone=sample()
# # newone.call()
# # print()
# # del newone
# # newone.call()




# class employee:
#     "this is class employee"
#     rais=1.04
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.mail=first+last
#         self.pay=pay
#     def fullname(self):
#         return f"{self.first} {self.last}"  
#     def raiseamt(self):
#         return self.pay*self.rais
    

#     # class method
#     @classmethod
#     def setraisment(cls,val):
#         cls.rais=val
#     @classmethod
#     def obj_creator(cls,str):
#         a,b,c=str.split('-')
#         return cls(a,b,c)
#     @staticmethod
#     def weekday(year,month,day):
#         import calendar
#         t=calendar.weekday(year,month,day)
#         # print(t)
#         if t>4 :
#             print("its weekend")
#         else:
#             print("its weekday")
    
  


# # def weekday(year,month,day):
# #     import calendar
# #     t=calendar.weekday(year,month,day)
# #     print(t)
# #     if t>4 :
# #         print("its weekend")
# #     else:
# #         print("its weekday")
# # weekday(2023,7,15)
    

# # emp1=employee('devin','mathew',1000)
# # emp2=employee('dainty','mathew',2000)

# # str1="dev-sunny-32000"
# # str2='abylal-joy-40000'
# # str3='david-luke-50000'

# # # first,last,pay=str1.split("-")
# # emp3=employee.obj_creator(str1)

# employee.weekday(2023,7,15)



# #INHERITANCE

# # single inheritance
# class developer(employee):
#     rais=1.08
#     def __init__(self, first, last, pay,prolang):
#         super().__init__(first, last, pay)
#         self.prolang=prolang
  

# dev1=developer("devin","mathew",10000)
# # print(dev1.fullname())
# # print(dev1.raiseamt())
# emp1=employee('araa','ariyilla',1000)
# emp2=employee('dainty','mathew',2000)
# print(emp1.raiseamt())
# print(dev1.raiseamt())


# #########################
# @property

# class employee:
#     "this is class employee"
#     rais=1.04
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.mail=first+last
#         self.pay=pay
#     @property
#     def fullname(self):
#         return f"{self.first} {self.last}" 
#     @fullname.setter
#     def fullname(self,name):
#         first,last=name.split()
#         self.first=first
#         self.last=last 
#     @fullname.deleter
#     def print("delete name")
#     self.first=None
#     self.last=None
#     def raiseamt(self):
#         return self.pay*self.rais

# emp1=employee("devin","mathew",10000)
# emp1.fullname="dainty mathew"
# print(emp1.fullname)
# del emp1.fullname

################################

# class person:
#     def display(self):
#         print("this is class persosn")
# class employee(person):
#     def printing(self):
#         print("derived from class person")
# class programmer(employee):
#     def show(self):
#         print("derived from class employee")
# p1=programmer()
# p1.display()
# p1.printing()
# p1.show()

#######################################

# class landanimal:
#     def show(self):
# #         print("animal lives on land")
# # class wateranimal:
# #     def printing(self):
# #         print("animal lives in water")
# # class frog(landanimal,wateranimal):
# #     pass


# ###################################################
# # encapsulation

# # class car:
# #     __maxspeed=100
# #     def __init__(self) :
# #         self.__update()
# #     def drive(self):
# #         print(("lets go!!,drive"))
# #         print(self.__maxspeed)
# #     def __update(self):
# #         print("updating")
# #     def changespeed(self,speed):
# #         self.__maxspeed=speed
# # audi=car()
# # audi.changespeed(1000)
# # print(audi.drive())

#  #####################################

# # a=[1,2,3,4,5]
# # val=iter(a)
# # print(type(val))

# # print(next(val))
# # print(next(val))
# # print(next(val))
# # print(next(val))
# # print(next(val))

# # while True:
# #     try:
# #         print(next(val))
# #     except:
# #         break

# class m:
#     def __init__(self,s,e) :
#         self.start=s
#         self.end=e
    
#     def __next__(self):
#         if self.start<self.end:
#             if self.start==1:
#                 print(1)
#             else:
#                 print(self.start)
#             self.start+=1
#         else:
#             raise StopIteration      

        
        
# obj=m(1,10)      
# next(obj)
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))


#####################################
#generators

# def myrange(start):
#     current=start
#     while True:
#         yield current
#         current+=1
# reg=myrange(0)
# print(reg)
# print(next(reg))
# print(next(reg))
# print(next(reg))
# print(next(reg))
# print(next(reg))
# print(next(reg))
# print(next(reg))
# print(next(reg))

# class m:
#     def __init__(self,s) :
#         self.list=s.split()
        
    
#     def __next__(self):
#         res=iter(self.list)
            
#regular expression

import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (need to be escaped):
. ^ $ * + ? { } [ ] \ / ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
900-555-1234
Mr. Schafer
Mr Smith
ms Davis
Mrs. Robinson
Mr. T
cat 
pat 
mat
'''
# pattern=re.compile(r"abc")
# matches=pattern.finditer(text_to_search)
# for i in matches:
#     print(i)


# pattern=re.compile(r"\.")
# matches=pattern.finditer(text_to_search)
# for i in matches:
#     print(i)

# pattern=re.compile(r"\d")     #digits only
# matches=pattern.finditer(text_to_search)
# for i in matches:
#     print(i)

# pattern=re.compile(r"\D")    #except digit
# matches=pattern.finditer(text_to_search)
# for i in matches:
#     print(i)

# pattern=re.compile(r"\w")   # no special char only alpha and num
# matches=pattern.finditer(text_to_search)
# for i in matches:
#     print(i)

# pattern=re.compile(r"\W")   #only special char n space
# matches=pattern.finditer(text_to_search)
# for i in matches:
#     print(i)

# pattern=re.compile(r"\s")#only space tabspace newline 
# matches=pattern.finditer(text_to_search)
# for i in matches:
#     print(i)

# pattern=re.compile(r".")#anything
# matches=pattern.finditer(text_to_search)
# for i in matches:
#     print(i)


# pattern=re.compile(r"\bHa") #wordboundary 
# matches=pattern.finditer(text_to_search)
# for i in matches:
#     print(i)

# pattern=re.compile(r"\BHa")#nowordpoundary
# matches=pattern.finditer(text_to_search)
# for i in matches:
#     print(i) 

# sentance="Stars ens"
# pattern=re.compile(r"^Sta")#starts with
# matches=pattern.finditer(sentance)
# for i in matches:
#     print(i)

# pattern=re.compile(r"end$")
# matches=pattern.finditer(sentance)
# for i in matches:
#     print(i)

# pattern=re.compile(r"\d\d\d\W\d\d\d\W\d\d\d")
# matches=pattern.finditer(text_to_search)
# for i in matches:
#     print(i)
# pattern=re.compile(r"\d{3}.\d{3}.\d{4}")
# matches=pattern.finditer(text_to_search)
# for i in matches:
#     print(i)

# pattern=re.compile(r"\d{3}[-@]-\d{3}[-@].\d{4}")
# matches=pattern.finditer(text_to_search)
# for i in matches:
#     print(i)

# pattern=re.compile(r"[1-5]") #1 to 5 both included
# matches=pattern.finditer(text_to_search)
# for i in matches:
#     print(i)

# pattern=re.compile(r"[a-zA-z]")
# matches=pattern.finditer(text_to_search)
# for i in matches:
#     print(i)


# pattern=re.compile(r"(Mr|Mrs|Ms|ms)\.?\s\w*")
# matches=pattern.finditer(text_to_search)
# for i in matches:
#     print(i) 

urls='''
http://www.google.com
http://www.isro.com
http://youtube.com
http://www.nasa.gov
jhfhgfhg'''

# pattern=re.compile(r"\w+\W*\w*\.*\w+\.\w+")
# matches=pattern.finditer(urls)
# for i in matches:
#     print(i) 

#  + - one or more
#  * - zero or more
#  ? - zero or one

# pattern=re.compile(r"\w+\W*\w*\.*\w+\.\w+")
# matches=pattern.findall(text_to_search)
# for i in matches:
#     print(i)
# emails ='''
# miketyson@gmail.com
# henry.cavill@university.edu
# jason-321-statham@my-work.net
# mhghgfhgv'''
# pattern=re.compile(r"")
# matches=pattern.finditer(emails)
# for i in matches:
#     print(i)