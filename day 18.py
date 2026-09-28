#given a list l=[1,2,2,3,4,4,5,6] create a new dictionary where keys are numbers and values are number of occcurences
# l = [1, 2, 2, 3, 4, 4, 5, 6]
# d = {}
# for i in l:
#     d[i]=l.count(i)
# print(d)

#given a list l=[11,34,78,23,90,65]
#find the largest number
# l=[11,34,78,23,90,65]
# print(max(l))
# #find the second largest
# l.sort()
# print("Second largest:", l[-2])
# #find the smallest
# print(min(l))
# #find the second smallest
# l.sort()
# print("Second smallest:", l[1])
#
# l=[['arun',23,30000],['amal',25,50000],['anu',27,40000]]
#find the max salary
# salary=[]
# for i in l:
#     salary.append(i[2])
# print(max(salary))
# #find the minimum age
# age=[]
# for i in l:
#     age.append(i[1])
# print(min(age))

#solution by miss
# maximum=[max (i[2] for i in l)]
# minimum=[min (i[1] for i in l)]
# print(maximum)
# print(minimum)


#find the largest and smallest number without using built in function
# l=[23,45,67,12,90,78]
# max=l[0]
# for i in l:
#     if(i>max):
#         max=i
# print("maximum",max)
# min=l[0]
# for i in l:
#     if(i<min):
#         min=i
# print("minimum",min)

#remove duplicates
# l=[1,1,2,3,3,4]
# new=list(set(l))
# print(new)
# #without using set and order should be preserved
# new=[]
# for i in l:
#     if i not in new:
#         new.append(i)
# print(new)


#given 2 lists find common elements
l1=[13,27,30,42,57]
l2=[13,57,89,33,80]
print(list(set(l1).intersection(set(l2))))

#or
s1=set(l1)
s2=set(l2)
print(list((s1).intersection(s2)))