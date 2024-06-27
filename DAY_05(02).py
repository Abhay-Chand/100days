# Adding elements to the list
'''We can add a new element/list of elements to the list using the list methods such as append(), insert(), and extend().'''
my_list = list([5, 8, 'Tom', 7.50])

# Using append()
my_list.append('Emma')
print(my_list)

# append the nested list at the end
my_list.append([25, 50, 75])
print(my_list)

'''Use the insert() method to add the object/item at the specified position in the list. The insert method accepts two parameters position and object.'''

my_list = list([5, 8, 'Tom', 7.50])

# Using insert()
# insert 25 at position 2
my_list.insert(2, 25)
print(my_list)

# insert nested list at at position 3
my_list.insert(3, [25, 50, 75])
print(my_list)

#Using extend()
my_list = list([5, 8, 'Tom', 7.50])

# Using extend()
my_list.extend([25, 75, 100])
print(my_list)

