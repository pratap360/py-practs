# code with harry tuts 66

# diamond shape problem in multiple inheritace

class A:
	def met(self):
		print("This is the method from class A")

class B(A):
	def met(self):
		print("This is the method from class B")

class C(A):
	def met(self):
		print("This is the method from class C")

class D(B,C):
	def met(self):
		print("This is the method from class D")

# class D(C,B):
# 	pass 

a=A()
b=B()
c=C()
d=D()

d.met()