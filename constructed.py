class Employee:
    no_of_leaves=8

# this is the constructor
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

# ash=Employee()
bapi=Employee("Pratap",60000,"Instructor")
# ^^this will passes through init function

# ash.name="Ayush"
# ash.salary=5000
# ash.role="Student"

# bapi.name="Pratap"
# bapi.salary=60000
# bapi.role="Instructor"

# print(bapi.printdetails())
# print(ash.printdetails())

print(bapi.salary)
