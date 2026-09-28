#def a function that takes string as argument and returns a new dict where keys are words and values are length of words.call the fn and print dict
s="python is easy and fun"
def word(s):
    new={}
    for i in s.split():
        new[i]=len(i)
    return new
a=word(s)
print(a)


#def a fn that takes a number as argument and check whether that number is spy number or not
# def spy(n):
#     sum=0
#     prod=1
#     for i in str(n):
#         sum=sum+int(i)
#         prod=prod*int(i)
#     if sum==prod:
#         print("spy number")
#     else:
#         print("not spy")
# n=int(input("enter a number"))
# spy(n)

#keyword arguments
# def fun(n,a):
#     print("name",n)
#     print("age",a)
# fun("arun",23) # this is position arg type
# fun(n='arun',a=23)
# fun(a=23,n="arun") #this is also possible


#default parameter
# def fun(n,a=23):
#     print("name",n)
#     print("age",a)
# fun("arun")

#arbitary positional arguments
# def fun(*args):
#     print(args)
# fun(10,20)
# fun(10,20,30)
# fun(1,2,3,4,5)

#arbitary keyword arguments
# def fun(**kwargs):
#     print(kwargs)
# fun(a=10,b=20)
# fun(a=10,b=20,c=30)
# fun(a=10,b=20,c=30,d=40)

#define a function to find the sum of numbers using arbitary argument type
def add(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum
# a=add(10,20)
a=add(1,2,3,4,5)
print(a)