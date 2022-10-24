# code with harry tuts 67


# operator over loading in python 

class Employee:
    no_of_leaves=5
    
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return f"The name is (self.name). salary is (self.salary) and role is (self.role)"
        
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    def __add__(self,other):
    	return self.salary + other.salary

    def __truediv__(self,other):
    	return self.salary / other.salary

    def __repr__(self):
    	return f"Employee((self.name),(self.salary),(self.role))"

    def __str__(self):
    	return f"The name is (self.name). salary is (self.salary) and role is (self.role)"

# emp1=Employee("Bapi",450,"programmer")
# emp2=Employee("Raj",50,"claener")
# print(emp1 + emp2)
# print(emp1 / emp2)
emp1=Employee("Bapi",450,"programmer")
# print(repr(emp1))
print(str(emp1))