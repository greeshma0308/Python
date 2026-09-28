# #ordinal
# print(ord('M'))
# print(ord('0'))
# print(ord('r'))



# #if
# n=int(input('enter a number '))
# if n%2==0:
#     print('Number is even')


#else if
# #WAP to check whether the number is positive or negative
# n=int(input('enter a number '))
# if n>0:
#     print('Number is positive')
# else:
#     print('Number is negative')


#WAP to check whether the number is even or odd
# n=int(input('enter a number '))
# if n%2==0:
#     print(f'{n} is even')
# else:
#     print(f"{n} number is odd")


#WAP to check whether a number is divisible by 3
# n=int(input("Enter a number: "))
# if n%3==0:
#     print(f"{n} is divisible by 3")
# else:
#     print(f"{n} number is not divisible by 3")


#WAP to display a name if entered name contains letter 'n' else print no
# name=input("Enter a name: ")
# if 'n' in name:
#     print(name)
# else:
#     print('no')


#WAP TO DISPLAY A NAME IF THE ENTERED NAME STARTS WITH 'N' ELSE DISPLAY NO
# name=input("Enter a name: ")
# if name[0]=='N':
#     print('Name is',name)
# else:
#     print('no')


#WAP TO DISPLAY A LOCATION NAME IF ENTERED LOCATION CONTAIN WORD 'LAND' ELSE PRINT NO
# loc=input("Enter a name: ")
# if 'land' in loc:
#     print('The location:',loc)
# else:
#     print('no')


#WAP TO CHECK WHETHER THE NUMBER IS DIVISIBLE BY 5 AND ENDS WITH 5
# n=int(input("Enter a number: "))
# if n%5==0 and n%10==5:
#     print(f"{n} is divisible by 5")
# else:
#     print("no")


#WAP TO FIND THE GREATEST OF 2 NUMBERS
# n1=int(input("Enter first number: "))
# n2=int(input("Enter second number: "))
# if n1>n2:
#     print(f"{n1} is greater")
# else:
#     print(f"{n2} is greater")


#WAP to check whether the number is positive or negative or zero
# n=int(input('enter a number '))
# if n>0:
#     print(n,' is positive')
# elif n<0:
#     print(n,' is negative')
# else:
#     print("number is zero")


#WAP TO FIND THE GREATEST OF 3 NUMBERS
# n1=int(input("Enter first number: "))
# n2=int(input("Enter second number: "))
# n3=int(input("Enter second number: "))
# if n1>n2 and n1>n3:
#     print(f"{n1} is greatest")
# elif n2>n1 and n2>n3:
#     print(f"{n2} is greatest")
# else:
#     print(f"{n3} is greatest")


#WAP TO CHECK WHETHER A PERSON IS ELIGIBLE TO VOTE OR NOT
# age=int(input("Enter age: "))
# if age>=18:
#     print("Eligible to vote")
# else:
#     print("Not eligible")


#WAP TO CHECK WHETHER A NUMBER IS EVEN ODD OR INVALID
n=int(input('enter a number '))
if n%2==0:
    print(f'{n} is even')
elif n%2!=0:
    print(f"{n} number is odd")
else:
    print(f"{n} number is invalid")