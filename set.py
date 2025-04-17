#set

my_set={1,2,3,4,5}
print(my_set)

#add element
my_set.add(6)
print(my_set)


#remove element

my_set.remove(3)
print(my_set)


my_set1={1,2,3}
my_set2={3,4,5}

#union

union= my_set1|my_set2
print(union)

#intersection
intersection = my_set2 & my_set1
print(intersection)

#deffirenacetion
deffrentionset1= my_set1 - my_set2
deffrentionset2= my_set2-my_set1
print(deffrentionset1)
print(deffrentionset2)

