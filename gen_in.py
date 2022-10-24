# code with harry tuts 72 

# generator in python

"""
iterable - __iter__() or __getitem__()
iterator-__next__()
iteration-
"""

"""print , return, yeild """

def gen(n):
	for i in range(n):
		yeild i
g= gen(45)
print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# for i in g:
# 	print(i)
# note => int can't be iterable
h=harry
# print(h[0])
ier=iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
# for c in h:
# 	print(c)
