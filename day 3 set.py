#s={1,2,[1,2]}
#print(s) -> does not support heterogeneous data
s={1,2,3}
#print(s[1]) -> not supported
#s[2]=55 -> not supported
print(s)
s={1,2,3,4,5,5} #-> duplicates wont be printed
print(s)
#s.append(6) #-> does not support append
s.add(10)
s.add(20)
s.add(30)
print(s)

