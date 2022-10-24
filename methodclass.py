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


bapiu=Employee("Bapi",45,"Programmer")
ayushu=Employee("Ayush",14,"student")

ayush.change_leaves(35)

print(bapiu.no_of_leaves)
