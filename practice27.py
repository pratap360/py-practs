# map filter and reduce
# ------------------map-----------------------------
# no=["3","34","64"]
# no=list(map(int,no))
# for i in range(len(no)):
#     no[i]=int(no[i])
# no[2]=no[2]+1
# print(no[2])
# def sq(a):
#     return a*a
# num=[2,4,5,35,76,46,2,56,9]
# square=list(map(sq,num))
# print(square)

# num=[2,4,5,35,76,46,2,56,9]
# square=list(map(lambda x: x*x,num))
# print(square)


# def square (a):
#     return a*a
# def cube (a):
#     return a*a*a
# func=[square,cube]
# for i in range(5):
#     val=list(map(lambda x:x(i),func))
#     print(val)



# ----------------------------filter function----------------------------

# list_num=[1,2,3,4,5,6,7,8,9]
# def greater(num):
#     return num>5
# big_5=list(filter(greater,list_num))
# print(big_5)



# ----------------------------reduce----------------------------
# from functiontools import reduce

list_num=[1,2,3,4,5,6,7]
num=0
# for i in list_num:
#     num+=i
# or by using the reduce module or function
num=reduce(lambda x,y:x+y,list_num)
num=reduce(lambda x,y:x*y,list_num)
print(num)
