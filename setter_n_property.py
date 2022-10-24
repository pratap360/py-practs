# code with harry tuts 69

# setter and property decorators 

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


pratap_parui=Employee("Pratap","parui")
# hindustani_supporter=Employee("hindu","supporter")

# here property is the decorators
# print(pratap_parui.explain())

# print(pratap_parui.email())

# pratap_parui.fname="Bapi"

# print(pratap_parui.email())

print(pratap_parui.email)
pratap_parui.fname="Bapi"
print(pratap_parui.email)

pratap_parui.email="this.that@gmail.com"
print(pratap_parui.fname)
# print(pratap_parui.lname)
# print(pratap_parui.email)

del pratap_parui.email
print(pratap_parui.email)
pratap_parui.email="bapi.bapiu@gmail.com"
print(pratap_parui.email)