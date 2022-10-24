# # external and build in modules
import random

random_number=random.randint(0,15)
# print(random_number)
rand=random.random()*10
# print(rand)
lst=["zee bangla","hungama","diseny","nick","logic:Opideya"]
choice=random.choice(lst)
print(choice)

# run this code only any of 1 

# all about f string
import math
me="bapi"
a1=45
# a="this is %s"%me
# a="this is {} {}"
# b=a.format(me,a1)
# print(b)
a=f"this is {me} {a1} {math.sin(90)}"
print(a)
