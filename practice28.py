# virtual environment and requeriments
# we have to install from pip install virtualenv

# Take a list, say for example this one:
# a=[1,1,2,3,5,8,13,21,34,55,89]
# and write a program that prints out all the elements of the list that are less than 5.
# excepted output 1,1,2,3

# """1 way to do"""
# num1=[1,1,2,3,5,8,13,21,34,55,89]
# def lesser(num):
#     return num<5
# less_than=list(filter(lesser,num1))
# print(less_than)

# 2nd way to do it
num1=[1,1,2,3,5,8,13,21,34,55,89]
for item in num1:
    if item<5:
        print(item)
