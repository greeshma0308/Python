#FOR LOOP
#STRING
# s='morning'
# for i in s:
#     print(i)

# #LIST
# l=['apple','mango','grapes','kiwi']
# for i in l:
#     print(i)
#
# #SET
# set={10,20,30,40}
# for i in set:
#     print(i)
#
# #DICTIONARY
# d={'anju':22,'renju':30,'veena':27}
# for i in d:
#     print(i)
# for i in d.values():
#     print(i)
#
# l=[12,34,56,45,45,89,16,69,33]
# for i in l:
#     print(i)
# for i in l:
#     if(i%2==0):
#         print(i)
# for i in l:
#     if(i%5==0):
#         print(i)
# for i in l:
#     if '3' in str(i):
#         print(i)

# s='hello world'
# for i in s:
#     print(i,end=" ")
# print()
# vowels="aeiouAEIOU"
# for i in s:
#     if i not in vowels:
#         print(i,end=" ")
# print()

# Given a dictionary
# d={'n1':23,'n2':46,'n3':89,'n4':24}
# print each value
# print odd values
#
# d={'n1':23,'n2':46,'n3':89,'n4':24}
# for i in d.values():
#     print(i,end=" ")
# print()
# for i in d.values():
#     if i%2!=0:
#         print(i,end=" ")
# print()

# Given a list l=["red",'green','orange','blue','black','yellow']
# print each color
# print color starting with 'b'
# print color whose length is greater than 5

# l=["red",'green','orange','blue','black','yellow']
# for i in l:
#     print(i,end=" ")
# print()
# for i in l:
#     if i[0]=='b':
#         print(i,end=" ")
# print()
# for i in l:
#     if len(i)>5:
#         print(i,end=" ")
# print()

# Given a list l=[10,'arun','amal',35,3.6,6.9,89]
# print  string values
# print float values

# l=[10,'arun','amal',35,3.6,6.9,89]
# for i in l:
#     if type(i)==str:
#         print(i,end=" ")
# print()
# for i in l:
#     if type(i)==float:
#         print(i,end=" ")
# print()

# l=[45,78,90,12,67]
# sum=0
# for i in l:
#     sum=sum+i
# print('Sum:',sum)
# prod=1
# for i in l:
#     if i%2==0:
#         prod=prod*i
# print('Product:',prod)
# count=0
# for i in l:
#     if i%2!=0:
#         count=count+1
# print('Count:',count)

# for i in range(1,6):
#     print(i)
# for i in range(1,10,2):
#     print(i)

# #1,3,5,7,9
# for i in range(1,10,2):
#     print(i,end=" ")
# print()
#
# #2,4,6,8,10
# for i in range(2,11,2):
#     print(i,end=" ")
# print()
#
# #1,4,9,16,25
# for i in range(1,6):
#     print(i**2,end=" ")
# print()
#
# #4,9,14,19,24,29,34,39
# for i in range(4,40,5):
#     print(i,end=" ")
# print()
#
# #5,4,3,2,1
# for i in range(5,0,-1):
#     print(i,end=" ")
# print()
#
# #8,6,4,2,0
# for i in range(8,-1,-2):
#     print(i,end=" ")
# print()
#
# #7,14,21,28,35,42
# for i in range(7,43,7):
#     print(i,end=" ")
# print()

#100,200,...,1000
# for i in range(100,1001,100):
#     print(i,end=" ")
# print()
#
#
# #1,8,27,64,125
# for i in range(1,6):
#     print(i**3,end=" ")
# print()
#
# #find all 3 digit numbers divisible by 3
# for i in range(100,1000):
#     if i%3==0:
#         print(i,end=" ")
# print()
#
# #print reverse of each colour
# colour=['red','green','blue','yellow','black']
# for i in colour:
#     print(i[::-1],end=" ")
# print()

#print each digit of a number
# n=1234
# for i in str(n):
#     print(i, end=" ")
# print()
