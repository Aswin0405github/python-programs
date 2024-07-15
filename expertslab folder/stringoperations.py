a="Aswin in the class"
# \n,\t
# upper fuction changes all chars upper 
# lower function changes every chsr into lower
# "title" all words first char capitalise
# "capitalize" 
# count number ofthat string in the string
# index gives the index of the first occurence of the string
# isalpha check if the string just contain alphabets
# a.replace("1","e",2)      output:Aswen en the class
# alnum gives if alpha or numbers or both
# starswith true if the string start with the pattern given
# endswith true if the string ends with the pattern given
# a=[aswin,athira,richard] , res=' '.join(a), gives "aswin athira richard"
#template
from string import Template
h="mathew"
a=Template("hi iam devin $b")
print(a.substitute(b=h))

var1="its sunday"
var2="have a great day"
print(var1.replace("sunday",var2[var2.find("a great"):len(var2)]))
print(var2.split()[2]+" "+var1[var1.find("sunday"):len(var1)])







