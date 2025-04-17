#syntax
# dic= {'keyvalue1':'value1', 'keyvalue2':'value2','keyvalue3':'value3' .......}

my_dict ={'name': 'ram', 'age':25, 'city':'lucknow'}
print(my_dict)

#access a value by keyvalue
# 
# 
print(my_dict['name'])

#add key new value pairs

my_dict['job']= 'engineer'
print(my_dict)


#change value of key value

my_dict['job']= 'doctor'
print(my_dict)


#delete key value
del my_dict['job']
print(my_dict)