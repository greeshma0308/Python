#wap to create a list of 5 random 3 digit numbers
import random
new=[]
for i in range(0,5):
    num=(random.randint(100,1000))
    new.append(num)
print(new)

#wap to create a 5 digit random otp number
import random
otp=random.randint(10000,99999)
print(otp)
#wap to find the position of character in a string
s = input("Enter a string: ")
ch = input("Enter character: ")
if ch in s:
    print("Position:", s.index(ch))
else:
    print("character not present")

#define a function that takes string as an argument and returns a new dictionary where keys are characters and  values are count of each charcter
def char_count(s):
    d = {}
    for i in s:
        d[i]=s.count(i)
    return d
print(char_count("hello"))

#Define a function that takes string as argument and print the count of digits,spaces,letters in that string
def count(s):
    letters=0
    digits=0
    spaces=0
    for i in s:
        if i.isalpha():
            letters+=1
        elif i.isdigit():
            digits+=1
        elif i==' ':
            spaces+=1
    print("Letters:",letters)
    print("Digits:",digits)
    print("Spaces:",spaces)
count("Hello 123 World")