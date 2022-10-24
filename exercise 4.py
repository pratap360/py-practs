# exercise 4
# pattern printing
# input integer n
# boolean = true or false
# true n=5
# *
# **
# ***
# ****
# *****
# false n=5
# *****
# ****
# ***
# **
# *
# answer 1
"""print("how many row you want to print")
one=int(input())
print("type 1 or 0")
two=int(input())
new=bool(two)
if new==True:
    for i in range(1,one+1):
        for j in range(1,1+1):
            print("*",end=" ")
        print()
elif new==False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()"""

# answer 2
"""print("pattern printing")
num=int(input("how many row you want to print"))
print("enter 1 or 0")
bool_val=input("1 for true val and 0 for false val")
if bool_val=="1":
    for i in range(0,num+1):
        print("*")
if bool_val=="0":
    for i in range(num,0,-1):
        print("*")"""

# answer 3
m=int(input("add number of lines you want to print"))
n=bool(int(input("add 0 for false")))
def star(m,n):
    if n==True:
        o=1
        while o<=m:
            print(o*"*")
            o=o+1
    else:
        while m>0:
            print(m,"*")
            m=m-1
star(m,n)
