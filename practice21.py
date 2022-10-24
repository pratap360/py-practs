# args and kwargs
#
# def funky_name_print(a,b,c,d):
#     print(a,b,c,d)
# funky_name_print("ayushu","bapiu","momiu","dadiu")

def funargs(normal,*args,**kwargs):
    # print(args[0])
    print(normal)

    for item in args:
        print(item)
        print("\nnow i would like to intro some of nature powers")
    for key,value in kwargs.items():
        print(f"{key} is a {value}")

name=["ayushu","bapiu","momiu","dadiu","mr_nobody"]
normal="I am normal arguments and the funky names are:"
kw={"ayushu":"notyboy","bapiu":"crazy programmer","momiu":"supermom","dadiu":"hwork"}
funargs(normal,*name,**kw)
