# try and exception
print("enter first no: ")
num_1=input()
print("enter second no: ")
num_2=input()
try:
    print("the sum of the no is ", int(num_1)+int(num_2))
except Exception as e:
    print(e)
