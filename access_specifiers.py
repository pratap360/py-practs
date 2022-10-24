# code with harry tuts 63
# access_specificers i.e :- public , private , protected 

# public - door or out side 
 
# protected - house 

# private - room 

class Employee:
	# public variable
    no_of_leaves = 8
    var=7
    # procted variable			
    _protecd=9
    # private variable
    __private=15

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

emp=Employee("bapi",343,"programmer")
# accessing the protected value
print(emp._protecd)
# accessing the private value
print(emp._Employee__private)	

