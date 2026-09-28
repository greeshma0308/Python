#write a program to find BMI(Body Mass Index)
# BMI= weight in (kg)/ height**2 in (m)
# BMI	                 Status
# ≤ 18.4	             Underweight
# 18.5 - 24.9	         Normal
# 25.0 - 39.9	         Overweight
# ≥ 40.0	             Obese

weight=float(input('Enter the weight'))
height=float(input('Enter the height'))
BMI=weight/(height**2)
if BMI<=18.4:
    print('Underweight')
elif BMI>=18.5 and BMI<=24.9:
    print('Normal')
elif BMI>=25.0 and BMI<=39.9:
    print('Overweight')
elif BMI>=40.0:
    print('Obese')


#2)# A toy vendor supplies three types of toys:
# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.
#The vendor gives a discount of 10% on orders for battery-based toys if the order is more than Rs.1000
#On orders of more than Rs.100 for key-based oys, a discount of 5% is given,
#and a discount of 10% is given on electrical charging based toys of value more than Rs.500
#Assume that the numeric codes 1,2 and 3 are used for battery based toys,key based toys and electrical charging based toys respectively
#Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount

code=int(input("Enter product code: "))
amount=float(input("Enter the amount: "))
if code==1:
    if amount>1000:
        d=amount*0.10
    else:
        d=0
elif code==2:
    if amount>100:
        d=amount*0.05
    else:
        d=0
elif code==3:
    if amount>500:
        d=amount*0.10
    else:
        d=0
else:
    print("Invalid product code")
net_amount=amount-d
print("Net amount to be paid:", net_amount)



#3 FIZZBUZZ Problem
# if divisible by 3 only -print fizz
# if divisible by 5 only -print buzz
# if a number is divisible by 3 and 5
#     print fizzbuzz
#     otherwise -print the number

n=int(input("Enter a number: "))
if n%3==0:
    if n%5==0:
        print('fizzbuzz')
    else:
        print('fizz')
elif n%5==0:
    print('buzz')
else:
    print(n)


