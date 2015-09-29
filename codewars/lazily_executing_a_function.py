# Deferring a function execution can sometimes save a lot of execution time in our programs by postponing the execution to the latest possible instant of time, when we're sure that the time spent while executing it is worth it.

# Write a method make_lazy that takes in a function (symbol for Ruby) and the arguments to the function and returns another function (lambda for Ruby) which when invoked, returns the result of the original function invoked with the supplied arguments.

# For example:

# Given a function add

# function add (a, b) {
#   return a + b;
# }
# One could make it lazy as:

# var lazy_value = make_lazy(add, 2, 3);
# The expression does not get evaluated at the moment, but only when you invoke lazy_value as:

# lazy_value() => 5
# The above invokation then performs the sum.

# Please note: The functions that are passed to make_lazy may take one or more arguments and the number of arguments is not fixed.


def add(a, b):
    return a + b

def make_lazy(*args):
    f = args[0]
    def lazy():
        return f(*args[1:])
    return lazy

f = make_lazy(add, 1, 3)

print f()


# 以下是别人的解答
# def make_lazy(f, *args, **kwargs):
#     return lambda: f(*args, **kwargs)

# Python 支持一种有趣的语法，它允许你快速定义单行的最小函数。这些叫做 lambda 的函数，是从 Lisp 借用来的，可以用在任何需要函数的地方。
