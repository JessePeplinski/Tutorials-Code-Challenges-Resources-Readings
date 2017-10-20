import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func(): #wraps around the function
        print("in decorator")
        func()
        print("after decorator")
    return function_that_runs_func

# apply my_decorator to my_function, changes my_function. 
@my_decorator
def my_function():
    print('im the function')

my_function()

## some more complex decorator, they can accept args themselves


def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func():
            print("in dec")
            
            if number == 56:
                print('not running func')
            else:
                func()
                
            print("after dec")
        return function_that_runs_func
    return my_decorator

@decorator_with_arguments(56)
def my_function_too():
    print("hello")

my_function_too()
