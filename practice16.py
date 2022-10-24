# more on python file
"""
f=open("bapi.txt")
# print(f.tell())
print(f.readline())
f.seek(0)
# print(f.tell())
print(f.readline())
# print(f.tell())
f.close()
"""
# with block
with open("bapi.txt") as f:
    a=f.read(5)
    print(a)
# f=open("bapi.txt")
# print(f.readline())
# f.close()
