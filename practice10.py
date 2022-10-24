#For loops in python using list
#Cats=["Tom","Tim","Rimijimi","Patapeti","Sundori"]
"""Cats=[["Tom",2],["Tim",1],["Rimijimi",0],["Patapeti",2],["Sundori",100]]
for item,chicken in Cats:
	print(item,"eats only",chicken,"Chicken")"""

#For loops in python using dictonry 
"""print("__________________________________")
Cats=[["Tom",2],["Tim",3],["Rimijimi",5],["Patapeti",0],["Sundori",10]]
dict1=dict(Cats)
for item,Fish in dict1.items():
	print(item,"eats only",Fish,"Fish")
"""
#quizes

l2=[int,float,"pratap",22,66,4,3,78,50,45,6]
for item in l2:
	if str(item).isnumeric() and item>6:
		print(item)