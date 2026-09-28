# #set
# s="python coding  is easy and fun"
# new={i for i in s if i in 'aeiou'}
# print(new)
#
#
# #dictionary comprehension
# l=[1,2,3,4]
# new={i:i**2 for i in l}
# print(new)

# l=[10,20,30,40]
# new={i:l[i] for i in range(0,len(l))}
# print(new)
#
# s='python is a simple language'
# for i in s.split():
#     print(i)

s='python coding is easy and fun'
new={i:len(i) for i in s.split()}
print(new)

#FUNCTION
# def add():
#     "Addition of 2 numbers"  #docstring
#     n1 = int(input("Enter a number:"))
#     n2 = int(input("Enter a number:"))
#     s = n1 + n2
#     print(s)
#     return
# add()

#define a fn to display "hello your name"
# def name():
#     n=input("enter your name:")
#     print("hello",n)
# name()


#define a function to find the factorial of a number
# def factorial():
#     i=1
#     n=int(input("enter a number "))
#     fact=1
#     while(i<=n):
#         fact=fact*i
#         i=i+1
#     print("factorial:",fact)
#     return
# factorial()


#define a function to find the count of a specific character in a given string
# def count_char():
#     s=input("Enter a string: ")
#     ch=input("Enter the character: ")
#     count=0
#     for i in s:
#         if i==ch:
#             count+=1
#     print("Count=",count)
# count_char()

#define a fn to check whether a number is prime or not
# def prime():
#     n=int(input("enter a number:"))
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 print("not prime")
#                 break
#         else:
#             print("prime")
#     else:
#         print("neither prime nor composite")
# prime()
