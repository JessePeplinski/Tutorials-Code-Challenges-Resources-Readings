my_variable = "hello"

# we can get at the indiviual letters
print(my_variable[0]) # prints the h

# iterables --> strings, lists, ets, tuples, etc..
for char in my_variable:
    print(char)

my_list =[1,2,3,4,5]

for num in my_list:
    print(num * 2)

user_wants_num = True
while user_wants_num == True:
    print(10)

    user_input = input("Should we print again? (y/n) ")
    if user_input == 'n':
        user_wants_num = False


