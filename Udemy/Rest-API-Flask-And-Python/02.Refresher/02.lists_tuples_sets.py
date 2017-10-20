my_variable = 'hello'

grade_one = 77
grade_two = 80
grade_three = 70

print((grade_one + grade_two + grade_three) / 3) # this requires a lot of variables...

# so instead

grades = [70, 60, 80, 90, 80] # list 
tuple_grades = (60, 30, 80, 40) # delcared with (), tuple is immmutable, cannot increase the size
set_grades = {60, 30, 70, 80} # collection of unique and unordered elements, set operations

print(len(grades)) # return length, 5
print(sum(grades)) # return sum 

# some stuff you can do with lists 
grades.append(100) # can append to list, but not to tuple

# tuple can be changed entirely
tuple_grades = tuple_grades + (100,) # adds another new tuple to the tuple. the comma is needed
print(tuple_grades)

# print the item at index 0 
print(grades[0]) 

# what if we try...
# tuple_grades[0] = 60 # doesn't work! immutable.

# sets..
# set_grades[0] = 30 # which one is it? this doesn't work either

# but we can add things to a set
set_grades.add(30)

## Set opperations
your_lottery_numbers = {1,2,3,4,5}
winning_numbers = {1,3,5,7,9,11}

print(your_lottery_numbers.intersection(winning_numbers)) # finds the intersection of the two sets 
print(your_lottery_numbers.union(winning_numbers)) # finds the union
print({1,2,3,4}.difference({1,2})) # shows the difference between the sets 

# Create a list, called my_list, with three numbers. The total of the numbers added together should be 100.
my_list = [25, 25, 50]

# Create a tuple, called my_tuple, with a single value in it
my_tuple = (10)

# Modify set2 so that set1.intersection(set2) returns {5, 77, 9, 12}
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 9, 12}       

print(set1.intersection(set2))



