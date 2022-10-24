# scope and global
# l=11 #global scope(sarkari paisa)
# def function1(n):
#     # l=5 #local scope (apana paisa)
#     global l
#     l=1+64
#     m=3
#     print(l,m)
#
#     print("this is print function",n)
# function1("this is the function1")
# # print(l)

x=89
def bapi():
    x=45 #this is the local variable of the bapi function
    def ayushu():
        global x
        x=14
    print("roll no of bapi()",x)
    ayushu()
    print("roll no of ayushu()",x)
bapi()
print(x)
