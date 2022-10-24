# enumerate program
g1=["bendi","aloo","noodles","tendi"]

# i=1
# for item in g1:
    # if i%2 is not 0:
        # print(f"karwish PLEASE buy {item}")
    # i+=1

for index, item in enumerate(g1):
    if index%2==0:
        print(f"karwish PLEASE buy {item}")
