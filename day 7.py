#   WAP TO CHECK WHETHER THE ENTERED DIGIT IS 2 DIGIT/ 3 DIGIT/ 4 DIGIT
# n=int(input('Enter a number: '))
# if n>=10 and n<=99:
#     print(f'{n} is a 2 digit number')
# elif n>=100 and n<=999:
#     print(f'{n} is a 3 digit number')
# elif n>=1000 and n<=9999:
#     print(f'{n} is a 4 digit number')
# else:
#     print(f'{n} is not a 2/3/4 digit number')


#WAP A BASIC CALCULATOR PRGM TO PERFORM ARITHMETIC OPERATIONS
# n1=int(input("Enter first number: "))
# n2=int(input("Enter second number: "))
# op = input("Enter operator (+, -, *, /, %, //): ")
# if op=='+':
#     print(f'the sum is {n1+n2}')
# elif op=='-':
#     print(f'the difference is {n1-n2}')
# elif op=='*':
#     print(f'the product is {n1*n2}')
# elif op=='/':
#     print(f'the quotient is {n1/n2}')
# elif op=='%':
#     print(f'the remainder is {n1%n2}')
# elif op=='//':
#     print(f'the floor value is {n1//n2}')

#WAP TO PRINT THE NUMBER OF DAYS IN A MONTH
# l1=['January','March','May','July','August','October','December']
# l2=['April','June','September','November']
# l3=['February']
# month=input('Enter a month')
# if month in l1:
#     print(f'{month} has 31 days')
# elif month in l2:
#     print(f'{month} has 30 days')
# elif month in l3:
#     print(f'{month} has 28 or 29 days')

#Grades
n=int(input('Enter the mark'))
if  n>=91 and n<=100:
    print("Grade A")
elif n>=81 and n<=90:
    print("Grade B")
elif n>=71 and n<=80:
    print("Grade C")
elif n>=61 and n<=70:
    print("Grade D")
elif n<61:
    print("Grade E")