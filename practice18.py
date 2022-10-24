# recursions recursice and iterative approach
# def print2(str1):
#     print2(str1) """this will give a recursions error or depth execcepted"""
#     print("this is "+str1)
# print2("bapiu")

# def print2(str1):
#     print("this is "+str1)
# print2("bapiu")

# n!=n*n-1*n-2*n-3.....
# n!= n*(n-1)!
# def factorial_iterative(n):
#     fac=1
#     for i in range(n):
#         fac=fac*(i+1)
#     return fac
#
# def factorial_recursiive(n):
#     if n==1:
#         return 1
#     else:
#         return n* factorial_recursiive(n-1)
# num=int(input("enter the number:\n"))
# print(factorial_iterative(num))
# print(factorial_recursiive(num))

"""
how does the recursions work ?
if n==1: //if user input 5 number
    return 1
else:
    return n* factorial_recursiive(n-1)


5* factorial_recursiive(4)
5*4 factorial_recursiive(3)
5*4*3 factorial_recursiive(2)
5*4*3*2 factorial_recursiive(1)
5*4*3*2*1=120

"""

# quiz to make fibonacci series 0 1 1 2 3 5 8 13 21...
# def  fibonacci(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# num=int(input())
# print(fibonacci(num))

# normal pracitce
