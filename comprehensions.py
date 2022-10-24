# code with harry tuts 73

# comprehensions in python 

# ls= []
# for i in range(100):
# 	if i%3==0:
# 		ls.append(i)


# ls=[i for i in range(100) if i%3==0]
# print(ls)

# dict1={i:f"item{i}" for i in range(1,1000) if i%100==0}
# print(dict1)

# dict1={i:f"item{i}" for i in range(5)}
# dict2={value:key for key,value in dict1.items()}
# print(dict1,"\n",dict2)

# dresses ={dress for dress in ["dress1","dress2","dress1","dress2","dress1","dress2"]}
# print(dresses)
# print(type(dresses))

evens =(i for i in range(100) if i%2==0)
print(evens)
