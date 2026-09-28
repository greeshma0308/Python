#declare a list of 5 colours
#add a new colour yellow to the list
#change the second colour to black
#print the list in reverse order
#print the second last colour
#print the number of colours
#print the updated list

list=['pink','purple','blue','green','red']
print(list)
list.append('yellow')
print(list)
list[1]='black'
print(list)
print(list[::-1])
print(list[-2])
print(len(list))
print(list)