# lamda function or anonymous funcions
"""def add (a,b):
    return a+b

# minus= lambda x,y: x-y
# or
def minus (x,y):
    return x-y

print(minus(9,5))"""

# def a_first(a):
#     return a[1]
a=[[1,14],[5,3],[8,35]]
a.sort(key=lambda x:x[1])
print(a)
