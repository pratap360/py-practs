#all about sets
s=set()
#print(type(s))
#p=[1,2,3]
#s_from_list= set(p)
#print(s_from_list)
#print(type(s_from_list))
s.add(2)
s.add(4)
s.remove(2)
print(s)
#s1=s.union({44,25,66})
#s1=s.intersection({44,25,66})
#print(s, s1)
#print(len(s))
#print(min(s))
#print(max(s))
s1={3,6}
print(s.isdisjoint(s1))