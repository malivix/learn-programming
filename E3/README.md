# Episode 3
- Functions
- Recursive functions

# Functions
Functions are a way to group together a set of instructions that can be reused. They are defined using the `def` keyword. The syntax is as follows:

```python
def function_name(arg1, arg2, ...):
    # do something
    return something
```

## Function name (identifier)
- can be alphabet, number(non-negetive integer), underscore (_)
- can't be keyword -> python keyword list -> https://docs.python.org/3/reference/lexical_analysis.html#keywords -> these are reserved words.
- can't be start with number -> 1a, 2b, 3c, 4d, 5e, 121, 0asavasdvas

### Correct examples
- a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
- man, count, ...
- a1, b2, c3, d4, e5, f6, g7, h8, i9, j0, k11, l22, m33, n44, o55, p66, q77, r88, s99, t00, u111, v222, w333, x444, y555, z666
- V2, v2paafsn2

### Incorrect examples
- 1a, 2b, 3c, 4d, 5e, 6f, 7g, 8h, 9i, 0j, 11k, 22l, 33m, 44n, 55o, 66p, 77q, 88r, 99s, 00t, 111u, 222v, 333w, 444x, 555y, 666z
- False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

## Function name (identifier) convention in python
In python, function name is written in snake_case. Snake case is a naming convention in which all letters are lowercase and spaces are replaced with underscores. For example, `my_function_name`.
Function name that is written with underscore at beggining is called private function. Private function is a function that is not supposed to be called outside of the module. For example, `_my_private_function_name`.

#### examples
snake_case, snake_case_is_good, snake_case_is_good_for_python, snake_case_is_good_for_python_programming, snake_case_is_good_for_python_programming_language, snake_case_is_good_for_python_programming_language_so_you_should_use_it

## Function arguments
Function arguments are the values that are passed to the function when it is called. The function arguments are defined in the function definition. The function arguments are separated by commas. The function arguments are optional. If the function arguments are not defined, then the function can be called without any arguments.

### Function order arguments
Function order arguments are the arguments that are passed to the function in the same order as they are defined in the function definition. For example, if the function definition is `def function_name(arg1, arg2, arg3):`, then the function order arguments are `arg1`, `arg2`, `arg3`.
like this:
```python
function_name(1, 2, 3) -> arg1 = 1, arg2 = 2, arg3 = 3
function_name(1, 2) -> arg1 = 1, arg2 = 2, arg3 = None
function_name(1) -> arg1 = 1, arg2 = None, arg3 = None
function_name() -> arg1 = None, arg2 = None, arg3 = None
```

### Function keyword arguments
Function keyword arguments are the arguments that are passed to the function using the keyword. For example, if the function definition is `def function_name(arg1, arg2, arg3):`, then the function keyword arguments are `arg1=`, `arg2=`, `arg3=`.
like this:
```python
function_name(arg1=1, arg2=2, arg3=3) -> arg1 = 1, arg2 = 2, arg3 = 3
function_name(arg1=1, arg2=2) -> arg1 = 1, arg2 = 2, arg3 = None
function_name(arg1=1) -> arg1 = 1, arg2 = None, arg3 = None
function_name() -> arg1 = None, arg2 = None, arg3 = None
function_name(arg2=1, arg1=2) -> arg1 = 2, arg2 = 1, arg3 = None
function_name(arg3=3) -> arg1 = None, arg2 = None, arg3 = 3
```

### Function order and keyword arguments
Function order and keyword arguments are the arguments that are passed to the function in the same order as they are defined in the function definition and using the keyword. For example, if the function definition is `def function_name(arg1, arg2, arg3):`, then the function order and keyword arguments are `arg1`, `arg2=`, `arg3=`.
like this:
```python
function_name(1, arg2=2, arg3=3) -> arg1 = 1, arg2 = 2, arg3 = 3
function_name(1, arg3=3) -> arg1 = 1, arg2 = None, arg3 = 3
function_name(arg1=1, arg3=3) -> arg1 = 1, arg2 = None, arg3 = 3
function_name(1, 2, arg3=3) -> arg1 = 1, arg2 = 2, arg3 = 3
```

### Function default arguments
Function default arguments are the arguments that are defined with a default value in the function definition. For example, if the function definition is `def function_name(arg1, arg2=2, arg3=3):`, then the function default arguments are `arg2=2`, `arg3=3`.
like this:
```python
def function_name(arg1, arg2=20, arg3=30):
    print(arg1, arg2, arg3)

function_name(1) -> arg1 = 1, arg2 = 20, arg3 = 30
function_name(1, 2) -> arg1 = 1, arg2 = 2, arg3 = 30
function_name(1, 2, 3) -> arg1 = 1, arg2 = 2, arg3 = 3
function_name(1, arg3=3) -> arg1 = 1, arg2 = 20, arg3 = 3
function_name(1, arg2=2) -> arg1 = 1, arg2 = 2, arg3 = 30
function_name(1, arg2=2, arg3=3) -> arg1 = 1, arg2 = 2, arg3 = 3
function_name(1, arg3=3, arg2=2) -> arg1 = 1, arg2 = 2, arg3 = 3
```

### Function variable arguments
Function variable arguments are the arguments that are defined with a `*` in the function definition. For example, if the function definition is `def function_name(arg1, *args):`, then the function variable arguments are `*args`.
args is ordered by function call arguments order.
Variable arguments are passed as a tuple.

Note: as convention, the function variable arguments named `*args`.

like this:
```python
def function_name(arg1, *args):
    print(arg1, args)

function_name(1) -> arg1 = 1, args = ()
function_name(1, 2) -> arg1 = 1, args = (2,)
function_name(1, 2, 3) -> arg1 = 1, args = (2, 3)
```

### Function keyword variable arguments
Function keyword variable arguments are the arguments that are defined with a `**` in the function definition. For example, if the function definition is `def function_name(arg1, **kwargs):`, then the function keyword variable arguments are `**kwargs`.
Keyword variable arguments are passed as a dictionary.

Note: as convention, the function variable arguments named `**kwargs`.


like this:
```python
def function_name(arg1, arg2, arg3, **kwargs):
    print(arg1, kwargs)

function_name(1, 2, 3) -> arg1 = 1, arg2 = 2, arg3 = 3, kwargs = {}
function_name(1, 2, 3, arg4=4) -> arg1 = 1, arg2 = 2, arg3 = 3, kwargs = {'arg4': 4}
function_name(1, 2, mahdi=3) -> arg1 = 1, arg2 = 2, arg3 = None, kwargs = {'mahdi': 3}
```

### Function order and keyword variable arguments
Function order and keyword variable arguments are the arguments that are defined with a `*` and `**` in the function definition. For example, if the function definition is `def function_name(arg1, *args, **kwargs):`, then the function order and keyword variable arguments are `*args`, `**kwargs`.
Order and keyword variable arguments are passed as a tuple and a dictionary.

Note: as convention, the function variable arguments named `*args`, `**kwargs`.

like this:
```python
def function_name(arg1, *args, **kwargs):
    print(arg1, args, kwargs)

function_name(1) -> arg1 = 1, args = (), kwargs = {}
function_name(1, 2) -> arg1 = 1, args = (2,), kwargs = {}
function_name(1, 2, 3) -> arg1 = 1, args = (2, 3), kwargs = {}
function_name(1, 2, 3, arg4=4) -> arg1 = 1, args = (2, 3), kwargs = {'arg4': 4}
function_name(1, 2, mahdi=3) -> arg1 = 1, args = (2,), kwargs = {'mahdi': 3}
```

### Function in function
Function in function is a function that is defined inside another function. For example, if the function definition is `def function_name(): def function_name2(): pass`, then the function in function is `function_name2` and you can not call it outside of `function_name`.

like this:
```python
def function_name():
    def function_name2():
        print('function_name2')

    function_name2()
```
#### sample use case
This is a sample use case of function in function. This is a counter function that counts the number of times it is called.
We call this closure because the function in function has access to the variables of the outer function.
We will talk about closure in the next sections.
```python
def function_name():
    a = 0
    def function_name2():
        nonlocal a
        a += 1
        return a

    return function_name2

counter = function_name()

print(counter())
print(counter())
print(counter())
```

### Function return
Function return is the value that is returned from the function. For example, if the function definition is `def function_name(): return 1`, then the function return is `1`.
Function return is optional. If the function does not have a return statement, then the function call will return `None`.

like this:
```python
def function_name():
    return 1

print(function_name()) # -> 1
```
```python
def function_name():
    a = 1 * 2

print(function_name()) # -> None
```

#### Function return multiple values
Function return multiple values is the values that are returned from the function. For example, if the function definition is `def function_name(): return 1, 2`, then the function return multiple values is `1, 2`.
Function return multiple values is optional. If the function does not have a return statement, then the function call will return `None`.
Type of function return multiple values is tuple.

like this:
```python
def function_name():
    return 1, 2

print(function_name()) # -> (1, 2)
```
```python
def swap(a, b):
    return b, a

a = 1
b = 2
a, b = swap(a, b) # -> a = 2, b = 1
```

#### Tuple unpacking
Tuple unpacking is the ability to assign the items of a tuple to variables. For example, if the tuple is `a = (1, 2)`, then the tuple unpacking is `a1, a2 = a`.
Tuple unpacking is optional. If the tuple unpacking is not used, then the tuple will be assigned to a variable.

You can use * for unpacking the rest of the items in the tuple.

like this:
```python
a = (1, 2)
a1, a2 = a # -> a1 = 1, a2 = 2
```
```python
a = (1,2 ,3)
a1, a2 = a # -> ValueError: too many values to unpack (expected 2)
```
```python
a = (1, 2, 3)
a1, a2, a3 = a # -> a1 = 1, a2 = 2, a3 = 3
```
```python
a = (1, 2, 3)
a1, a2, a3, a4 = a # -> ValueError: not enough values to unpack (expected 4, got 3)
```
```python
a = (1, 2, 3)
a1, a2, a3, *a4 = a # -> a1 = 1, a2 = 2, a3 = 3, a4 = []
```

### pass statement
pass statement is a statement that does nothing. It is used as a placeholder when a statement is required syntactically but the program requires no action.

like this:
```python
def function_name():
    pass

print(function_name()) # -> None
```

### Function recursion
Function recursion is a function that calls itself. For example, if the function definition is `def function_name(): function_name()`, then the function recursion is `function_name`.

Note: function recursion must have a base case to stop the recursion.

like this:
```python
def function_name():
    function_name()

function_name() # -> RecursionError: maximum recursion depth exceeded
```

we wnat to calculate the sum of n numbers. for example, if n = 5, then the sum is 1 + 2 + 3 + 4 + 5 = 15.
```python
def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)

print(sum(5)) # -> 15
print(sum(10)) # -> 55
```