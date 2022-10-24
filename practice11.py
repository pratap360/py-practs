# if else and elif loop
"""var1=56
var2=6
var3=int(input())
if var3>var1:
	print("it is greater")
elif var3==var1:
	print("it is equal")	
else:
	print("it is lesser")
"""
"""list1=[4,6,8,2,5]
print(10 not in list1)
if 5 in list1:
	print("yea it is there")
"""
# quiz
"""
print("what is your age: ")
age=int(input())
if age<18:
	print("you can not drive")
elif age==18:
	print("we will think about it")
else:
	print("yes u can drive")
"""
# short hand if else
a=int(input("enter a\n"))
b=int(input("enter b\n"))
#if a>b:	print("A B se bada hai bahi")
print("B A se Bada hai bahi") if a<b else print("A B se bada hai bahi")
