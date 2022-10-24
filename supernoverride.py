# code with harry tuts 65

# super and overriding and method over riding in class 

class A:
	classvar1="I am a class var in class A"
	def __init__(self):
		self.var1="I am inside class A's constructor"
		self.classvar1="Instance var in class A"
		self.special="special"

class B(A):
	classvar1="I am in class B"
	def __init__(self):
		# super().__init__()
		self.var1="I am inside class B's constructor"
		self.classvar1="Instance var in class B"
		super().__init__()
		print(super().classvar1)

# class are called 
# this are the object of the class 
a=A() 
b=B()

# print(b.classvar1)
# print(b.special)
print(b.special, b.var1, b.classvar1)