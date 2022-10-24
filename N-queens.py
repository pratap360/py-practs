from itertools import permutations

# txt=list(permutations('SKIN'))
# t = [''.join(i) for i in txt]
# print(t)

N=8
sol=0
cols=range(N)
for combo in permutations(cols):
    if N==len(set(combo[i]+i for i in cols))==len(set(combo[i]-i for i in cols)):
        sol +=1
        print("solution..."+str(sol)+ ":" + str(combo)+ "\n")
        print("\n".join('o' * i + 'X'+'o'*(N-i-1) for i in combo)+"\n\n\n\n")