# code with harry tuts 76
# try and except with else 

f1= open ("bapi.txt")
try:
    f= open("does.txt")
    
except EOFerror as e:
    print("print eof error aa gaya hai")

except IOerror as e:
    print("print io error aa gaya hai")    
    
# except exception as e:
#     print(e)
    
else:
    print("this will run only if exvept is not running")
    
finally:
    print("run this anyway...")
    # f.close()
    f1.close()

print("important stuff")
