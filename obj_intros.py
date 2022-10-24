# code with harry tuts 70 

# object introspection 

class Employee:
	def __init__(self,fname,lname):
		self.fname=fname
		self.lname=lname
		# self.email=f"{fname}.{lname}@gmail.com"

	def explain(self):
		return f"This Employee is {self.fname} {self.lname}"

	@property
	def email(self):
		if self.fname==None or self.lname==None:
			return "email is not set pls set it using setter"
		return f"{self.fname}.{self.lname}@gmail.com"

	@email.setter
	def email(self,string):
		print("setting now..")
		names=string.split("@")[0]
		self.fname=names.split(".")[0]
		self.lname=names.split(".")[1]
		
	@email.deleter
	def email(self):
		self.fname=None
		self.lname=None

skillf=Employee("skill","F")
# print(skillf.email)
# print(type(skillf))
# print(id(skillf))

# print(id("this is the string"))
# print(id("that is the string"))

O="this is the string"
# print(dir())
# print(dir(O))
# print(dir(skillf))

import inspect
print(inspect.getmembers(skillf))