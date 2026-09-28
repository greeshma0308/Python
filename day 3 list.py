list=[101,102,103]
lst=[106]
print(list)
list.append(800) #list is mutable
print(list)
list.append(800) #repetition of elements is allowed
print(list)

lst=[1,"name",30.5,5]
print(lst[1])
lst[1]='anju'
print(lst)
lst.append(100000)
print(lst)
print(lst[-1]) #last element
print(lst[-2]) #second last element
print(lst[1:]) #prints from first index