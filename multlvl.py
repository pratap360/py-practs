# code with harry 
# multiple level inhertiance 

class Dad:
	basketball=1

class Son(Dad):
	dance=1
	basketball=10
	def isdance(self):
		return f"yes i can do dance {self.dance} no of times"


class Grandson(Son):
	dance=6

	def isdance(self):
		return f"yes i can do awesome dance {self.dance} no of times"

dary=Dad()
larry=Son()
harry=Grandson()

print(harry.basketball)