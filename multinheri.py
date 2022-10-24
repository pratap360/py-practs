# code with harry tuts 


class Employee:
    no_of_leaves = 8
    var=7

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




class Player:
	no_of_games=4
	var=9
	def __init__(self,name,game):
		self.name=name
		self.game=game

	def printdetails(self):
		return f"The Name is {self.name}. Salary is {self.game}"


class coolProgramer(Employee,Player):
	language="c++"
	var=10
	def printlanguage(self):
		print(self.language)

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
		
shub=Player("shub",["chess"])
karan = coolProgramer("karan",8999,"coolProgramer")
det=karan.printdetails()
karan.printlanguage()

print(det)
