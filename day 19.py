#lambda
#sum of 2 numbers
# x=lambda a,b:a+b
# print(x(50,60))
#
# #product of 3 numbers
# x=lambda a,b,c:a*b*c
# print(x(5,6,7))
#
# #First letter of a string
# a=lambda s:s[0]
# print(a("hello"))
#
# l=[1,2,3,4]
# print(list(map(lambda x:x**2,l)))
# print(tuple(map(lambda x:x**2,l)))
# print(set(map(lambda x:x**2,l)))


#create a new list of cubes
# l=[1,2,3,4]
# print(list(map(lambda x:x**3,l)))
#
# #create a new list of square roots
# l=[25,36,81,100]
# print(list(map(lambda x:x**0.5,l)))
#
#
# #create a new list of lengths
# colors=['red','green','blue','yellow','black']
# #create a new list of first characters
# print(list(map(lambda x:x[0],colors)))
# #create a new list of last characters
# print(list(map(lambda x:x[-1],colors)))
# #create a new list of reverse of each element
# print(list(map(lambda x:x[::-1],colors)))

# #Given a list
# l=[23,78,12,56]
# #Add 10 to each element in the given sequence
# print(list(map(lambda x:x+10,l)))

# ##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},{'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},{'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
# # # create a new list of emails
# print(list(map(lambda x:x['email'],l)))

#questions in notebook
#filter
# l=[23,45,67,12,89,70]
# print(list(filter(lambda x:x%2==0 and x>50,l)))
#
# colors=['red','green','blue','yellow','orange']
# print(list(filter(lambda x:len(x)>5,colors)))
# print(list(filter(lambda x:'n' in x,colors)))

#reduce
#sum
l=[1,2,3,4]
import functools
a=functools.reduce(lambda x,y:x+y,l,0)
print(a)