#
# CS1010S --- Programming Methodology
#
# Mission 3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.


###########
# Task 1a #
###########

def combine(f, op ,n):
    result = f(0)
    for i in range(n):
        result = op(result, f(i))
    return result

def smiley_sum(t):
    def f(x):
        ...

    def op(x, y):
        ...

    n = ...

    # Do not modify this return statement
    return combine(f, op, n)


###########
# Task 1b #
###########

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def new_fib(n):
    def f(x):
        ...

    def op(x, y):
        ...

    # Do not modify this return statement
    return combine(f, op, n+1)

# Your answer here:
# 


##########
# Task 2 #
##########

# Time complexity: O(...)
# Space complexity: O(...)


##########
# Task 3 #
##########

# Time complexity of bar: O(...)
# Time complexity of foo: O(...)

# Space complexity of bar: O(...)
# Space complexity of foo: O(...)

def improved_foo(params):
    # Fill in code here
    return

# Improved time complexity: O(...)
# Improved space complexity: O(...)
