# #WHILE LOOP
# i=1
# while(i<=5):
#     print(i)
#     i=i+1
#
# #1,3,5,7,9,11
# i=1
# while(i<=11):
#     print(i)
#     i=i+2
#
# #2,4,6,8,10,12
# i=2
# while(i<=12):
#     print(i)
#     i=i+2
#
#
# #1,4,9,16,25
# i=1
# while(i<=5):
#     print(i**2)
#     i=i+1
#
#
# #5,4,3,2,1
# i=5
# while(i>=1):
#     print(i)
#     i=i-1
#
#
# #1,4,7,10,13,16
# i=1
# while(i<=16):
#     print(i)
#     i=i+3
#
#
# #10,20,30,40,50,60,70,80
# i=10
# while(i<=80):
#     print(i)
#     i=i+10
#
# #3,6,9,12,15,18,21
# i=3
# while(i<=21):
#     print(i)
#     i=i+3
#
# #8,6,4,2,0
# i=8
# while(i>=0):
#     print(i)
#     i=i-2
#
#
# #100,101,102,.....200
# i=100
# while(i<=200):
#     print(i)
#     i=i+1

#print all 4 digit numbers(1000-9999)
# i=1000
# while(i<=9999):
#     print(i,end= ' ')
#     i=i+1
# print()


#print those number divisible by 3 in range (1-50)
# i=1
# while(i<=50):
#     if (i%3==0):
#         print(i)
#     i=i+1


#print those 3 digit numbers that are divisible by 5 and 7
# i=100
# while(i<=999):
#     if (i%5==0 and i%7==0):
#         print(i)
#     i=i+1


#print those numbers in range (100-200) which contains the digit 3
# i=100
# while(i<=200):
#     s=str(i)
#     if '3' in s:
#         print(i)
#     i=i+1

#count those number divisible by 3 in range (1-50)
# count=0
# i=1
# while(i<=50):
#     if (i%3==0):
#         count=count+1
#     i=i+1
# print(count)

#count those numbers in range (100-200) which contains the digit 3
# i=100
# count=0
# while(i<=200):
#     s=str(i)
#     if '3' in s:
#         count=count+1
#     i=i+1
# print(count)

#sum of 1,2,3,4,5
# i=1
# sum=0
# while(i<=5):
#     sum=sum+i
#     i=i+1
# print(sum)

# #product of series
# i=1
# prod=1
# while(i<=5):
#     prod=prod*i
#     i=i+1
# print(prod)

#sum of first 10 even numbers
i=1
sum=0
while(i<=20):
 if(i%2==0):
  sum=sum+i
 i=i+1
print(sum)

#PRODUCT OF FIRST 10 EVEN NUMBERS
i=1
prod=1
while(i<=20):
 if(i%2==0):
  prod=prod*i
 i=i+1
print(prod)