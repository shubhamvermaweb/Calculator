#syntax
# mylist=[. . . . . ]
my_list=[1,2,3,4,5,"red","black","white"]
print(my_list)
#access elementby index number
print(my_list[3])
print(my_list[5])


print(my_list[3:7])

#insert the element in list
my_list.append("green")
print(my_list)

#removing element in list by value

my_list.remove(3)
print(my_list)

#removing element in list by index
del my_list[7]
print(my_list)


#reverse the list items
my_list.reverse()
print(my_list)