#WAP TO CHECK THE FOLLOWING:
# 1)A NUMBER IS DIVISIBLE BY 2 AND 3
# 2)A NUMBER IS DIVISIBLE BY 2 AND NOT DIVISIBLE BY 3
# 3)A NUMBER IS DIVISIBLE BY 3 AND NOT DIVISIBLE BY 2
# 4)A NUMBER IS NOT DIVISIBLE BY 2 AND 3
#
# n=int(input("Enter a number: "))
# if n%2==0:
#     print('Entered number is divisible by 2')
#     if n%3==0:
#         print('Entered number is divisible by 3')
#     else:
#         print('Entered number is not divisible by 3')
# else:
#     print('Entered number is not divisible by 2')
#     if n%3==0:
#         print('Entered number is divisible by 3')
#     else:
#         print('Entered number is not divisible by 3')
#


#WAP TO CHECK POSITIVE EVEN OR ODD
# TO CHECK NEGATIVE EVEN OR ODD
n=int(input("Enter a number: "))
if n>0:
    print('The number is positive')
    if n%2==0:
        print('The number is even')
    else:
        print('The number is odd')
else:
    print('The number is negative')
    if n%2==0:
        print('The number is even')
    else:
        print("The number is odd")
