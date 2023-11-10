# Data Structures

#Lists
#order of elemnts is very important

my_list = ['list', 1, 'of', 2, 'mixed']

print(len(my_list))
print([1,2] == [2,1], '- Lists Comparison')

#Sets
# every element in the set need to be unique, duplicates are discarded
# the order of elements in sets does not matter
my_set = {1,2,3,4,5}

print(type(my_set))
print({1,2} == {2,1}, '- Setts Comparison')

#Tuples
# are very similar to lists
#can't be appended/modified
# They are memory efficient
#goo dfor storing lots of little things, likr x, y coordinates

my_tuple = (1,2,3)
len(my_tuple)

print((1,2) == (2,1), '- Tuples Comparison')

#Dictionaries
#

my_dictionary = {
    'apple' : 'A red fruit',
    'bear' : 'A scary animal'
}
print(my_dictionary['apple'])

#Sets and Dictionaries
# Both are defined with curly brackets
# Sets have unique values, dictionaries have unique keys
# the order doesn't matter