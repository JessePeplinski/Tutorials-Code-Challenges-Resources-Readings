def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77

print(methodception(add_two_numbers))

# lambda function, always in one line
print(methodception(lambda: 35 + 77))

my_list = [10, 20, 30, 40, 50]

print(list(filter(lambda x: x != 13, my_list))) # all the numbers that are not 13

(lambda x: x * 3)(5)

# or.. refactoring a bit.

def not_thirteen(x):
    return x != 13

print(list(filter(not_thirteen, my_list)))