def my_method(arg1, arg2):
    return arg1 + arg2

my_method(5,6)

def my_long_method(arg1, arg2, arg3):
    return arg1 + arg2 + arg3

def my_list_addition(list_arg):
    return sum(list_arg)

my_long_method(1, 2, 3)

my_list_addition([1, 2, 3])

# You can add unlimited number of arguments..
def addition_simplifed(*args):
    return sum(args)

addition_simplifed(1,2,3,2,3,2)

# kwargs = keyword arguments, assign params as you pass them in
def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

what_are_kwargs(12, 34, 56, name='jose', location='UK')

def more_kwargs(name, location):
    print(name)
    print(location)

# You can also assign params as you pass them in
more_kwargs(name='Jose', location='UK')

