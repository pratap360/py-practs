# time modules
import time
initial=time.time()
k=0
while (k<4):
    print("this is parui bro")
    time.sleep(2)
    k+=1
print("while loops times",time.time()-initial,"seconds")
initial2=time.time()
for i in range(5):
    print("this is parui bro")
print("for loops times",time.time()-initial2,"seconds")
localtime=time.asctime(time.localtime(time.time()))
print(localtime)
