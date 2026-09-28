#Write a program to check whether two entered numbers are equal or not
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
if n1==n2:
    print("the numbers are equal")
else:
    print("the numbers are not equal")


#Write a program to check whether two entered words are equal or not
n1=input("Enter first word: ")
n2=input("Enter second word: ")
if n1==n2:
    print("the words are equal")
else:
    print("the words are not equal")


#Write a program to find the maximum of two numbers
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
if n1>n2:
    print(f"{n1} is maximum number")
else:
    print(f"{n2} is maximum number")



#write a program to check whether the entered character is vowel or not
ch=input("enter your character")
vowel='AEIOUaeiou'
if ch in vowel:
    print('the entered character is vowel')
else:
    print('the entered character is not a vowel')


# #Write a program to check whether the entered country name contains word 'land'
loc=input("Enter a country name: ")
if 'land' in loc:
    print('The location:',loc)
else:
    print('the location does not contain land')


#write a program to check whether the entered number is 3 digit or not
n1=int(input("Enter a number: "))
if n1>=100 and n1<=999:
    print(f'{n1} is a 3 digit number')
else:
    print(f'{n1} is not a 3 digit number')


#write a program to check whether the entered string is  palindrome or not
s=input("enter a string: ")
if s==s[::-1]:
    print(f'{s} is a palindrome')
else:
    print(f'{s} is not a palindrome')


#Write a program to check whether a number is present in given list
l=[23,67,12,90]
n=int(input("Enter a number: "))
if n in l:
    print(f'{n} is present in the list')
else:
    print(f'{n} is not present in the list')


#Write a program to check whether a key is present in a dictionary or not
d = {101:'Arun', 102:'Amal', 103:'Anu'}
key=int(input("Enter the key: "))
if key in d.keys():
    print("Key is present")
else:
    print("Key is not present")


#Write a program to check whether the given password is strong/weak(if length lessthan 8 weak)
s=input("enter a password: ")
if len(s)>=8:
    print(f'{s} is strong')
else:
    print(f'{s} is weak')