#file io basic

# file read
"""
read mode
"r"- open file for reading (default)
"w"- open file for writing
"x"- creates file if not exists
"a"- add more content to a file
"t"- text mode (default)
"b"- binary mode
"+"- read and write mode
"""
"""
f=open("bapi.txt","rb")
content=f.read()
print(content)
f.close()
"""
"""
f=open("bapi.txt")
content=f.read(5)
print(content)
f.close()
"""
"""
f=open("bapi.txt")
content=f.read()
for line in content:
	print(line)
f.close()
"""
"""f=open("bapi.txt")
for line in f:
	print(line)
f.close()"""
"""
f=open("bapi.txt")
print(f.readlines())
#print(f.readline())
f.close()"""

#file write
"""
f=open("bapi.txt","a")
a=f.write("\nPraise the lord")
print(a)
f.close()
"""

#handle read and wite both
# f=open("bapi.txt","r+")
# print(f.read())
# f.write("Amen")
list=[1,1,2,3,5,8,13]
print(list[list[4]])
