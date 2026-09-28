# l=[10,20,30,40]
# for i in l:
#     for j in range(1,4):
#         print(i,end=" ")
#     print()

#1 1 1 1
#2 2 2 2
#3 3 3 3
# for i in range(1,4):
#     for j in range(1,5):
#         print(i, end=" ")
#     print()

# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

# for i in range(1,4):
#     for j in range(1,5):
#         print(j, end=" ")
#     print()

# * * * *
# * * * *
# * * * *
# * * * *
# for i in range(1,5):
#     for j in range(1, 5):
#         print("*", end=" ")
#     print()
#

# l=[['lion','tiger'],['cat','elephant']]
# for i in l:
#     print(i)
#     for j in i:
#         print(j)


# names=['kelly','alan','jeny']
# for i in names:
#     for j in range(1,4):
#         print(i,end=" ")
#     print()


# n=[1,2,3]
# q=['what','when','why']
# for i in n:
#     print(i)
#     for j in q:
#         print(j,end=" ")
#     print()

# d=[{'id':101,'name':"arun",'age':23},
# {'id':102,'name':"amal",'age':24},
# {'id':103,'name':"anu",'age':25}]
# print('ID  NAME  AGE')
# for i in d:
#     for j in i.values():
#         print(j,end=" ")
#     print()


# d={'id':101,'name':"arun",'age':23}
# for i,j in d.items():
#     print(i,j)


# *
# * *
# * * *
# * * * *
# for i in range(1,5):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()

# *
# ***
# *****
# *******
# for i in range(1,8,2):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i, end=" ")
#     print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# for i in range(1,5):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# ****
# ***
# **
# *
# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()

#print all prime numbers from the list
# l=[23,45,78,90,12,13,91]
# for i in l:
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)


# #find all prime number in the range 1-100
# for i in range(2,101):
#     for j in range(2, i):
#         if i%j==0:
#             break
#     else:
#         print(i,end=" ")
# print()

#find all armstrong numbers in the range 100-1000
# for i in range(100,1001):
#     sum = 0
#     l = len(str(i))
#     for j in str(i):
#         sum=sum+int(j)**l
#     if sum==i:
#         print(i)

