"""a=6
b=8
c=sum((a,b)) #build in function
print(c)
"""
def function1(a,b):
    print("u r in function1: ", a+b)
def function2(a,b):
    """ this is a doc string"""
    avg=(a+b)/2
    #print(avg)
    return avg
v=function2(5,6)
print(v)
print(function2.__doc__)
