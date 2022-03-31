li = []

'''
li = li + another_list # bad, two step process
li.append(single_item)
li.insert(index, single_item)
li.extend(another_list)
'''

'''
len(li)
li[start:stop:step]
'''

'''
li.count(item_to_count)

li.index(element_to_search, start_search_from_this_index,
         stop_search_upto_this_index)

# The index() method only returns the first occurrence of the matching element.

if_li_contains_item = item in li
'''

'''
del li[index]

li.remove(element_to_remove)
# The remove() method takes a value and removes the first occurrence of that value from the list. 

li.pop() # 'pops' the last element, returns the value
li.pop(index) # 'pops' elem at given index, returns value 

'''

a_tuple = ()
'''immmutable lists'''
another_empty_tuple = tuple()

not_a_tuple = (44)
this_is_the_way = (44,)

''' tuple packing '''
v = ('1', 2, 'c')
''' tuple unpacking '''
(x, y, z) = v


'''
(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7) 
'''

a_set = {1}
''' unordered and unique values '''
''' allows op as union, intersection etc. '''

an_empty_set = set()
''' be careful '''
not_empty_set_but_empty_dict = {}

some_list = []
converted_to_set = set(some_list)

'''
a_set.add(item)

a_set.update(another_set)
a_set.update(set_1,set_2,set_3)

# both operations just ignore duplicate values
'''

'''

a_set.discard(element) # doesn't raise exception
a_set.remove(element) # raises exception if element not present

a_set.pop()
a_set.clear()
'''
another_set = set()

'''

a_set.union(another_set)
a_set.intersection(another_set)
a_set.difference(another_set)
a_set.symmetric_difference(another_set)

'''

a_dict = {}
''' unordered set of key-value pairs. '''
