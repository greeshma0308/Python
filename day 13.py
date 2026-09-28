# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# for i in range(1,5):
#     for j in range(1,5):
#         print(j, end=" ")
#     print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10

# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+1
#     print()

# A
# B C
# D E F
# G H I J
# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()

# A
# B B
# C C C
# D D D D
# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k), end=" ")
#     k=k+1
#     print()

# A
# A B
# A B C
# A B C D

# for i in range(1,5):
#     k = ord('A')
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()

# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4

# 1 0 0 0
# 0 2 0 0
# 0 0 3 0
# 0 0 0 4
# for i in range(1,5):
#     for j in range(1,5):
#         if i==j:
#             print(i,end=" ")
#         else:
#             print(0,end=" ")
#     print()

# 1
# 1 0
# 1 0 1
# 1 0 1 0
# for i in range(0,5):
#     for j in range(1,i+1):
#         if j%2==0:
#             print(0,end=" ")
#         else:
#             print(1,end=" ")
#     print()

# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4
# for i in range(0,5):
#     for j in range(0, i+1):
#         print(j, end=" ")
#     print()

# h
# h e
# h e l
# h e l l
# h e l l o

# s='hello'
# for i in range(len(s)):
#     for j in range(i+1):
#         print(s[j],end=" ")
#     print()

#       *
#     * *
#   * * *
# * * * *
# k=3*2
# for i in range(1,5):
# #for printing space in each line
#     for p in range(1,k+1):
#         print(end=" ")
# #for printing star in each line
#     for j in range(1,i+1):
#         print('*',end=" ")
#     k=k-2
#     print()

#       *
#     *   *
#   *   *   *
# *   *   *   *
# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print('*',end="   ") #increasing the space gives pyramid
#     k=k-2
#     print()


for i in range(3, 0, -1):
    for j in range(1, i + 1):
        print('*', end=" ")
    print()


