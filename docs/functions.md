# Functions

!!! note "Batteries included"
    The Python documentation includes an excellent
    [tour of the standard library](https://docs.python.org/3/tutorial/stdlib.html).

This tutorial has made use of several built-in Python functions already,
including 
[`type()`](https://docs.python.org/3/library/functions.html#type),
[`set()`](https://docs.python.org/3/library/functions.html#func-set),
[`len()`](https://docs.python.org/3/library/functions.html#len),
and
[`range()`](https://docs.python.org/3/library/functions.html#func-range).

## positional arguments

The simplest form of a function call takes one or more _positional arguments_. 
For example, the
[`sorted()`](https://docs.python.org/3/library/functions.html#sorted)
function can be called with only a single positional argument

```python
a = [ 3, 1, 5, 4, 2]

sorted(a)
```

This function will return a sorted version of the input list `[ 1, 2, 3, 4, 5 ]`.

## keyword arguments

If you read through the documentation for the
[`sorted()`](https://docs.python.org/3/library/functions.html#sorted)
function, you'll see that it can accept two more _keyword_ arguments

```python
def sorted(iterable, key=None, reverse=False)
```

These arguments are optional since they've been defined with the default values 
`None` and `False`. You can however override either of these arguments by 
referencing it by _keyword_. For example, you can pass `reverse=True` to 
reverse the sort order

```python
sorted(a, reverse=True)
```

## Defining a function

Functions are defined using the 
[`def`](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
keyword, followed by the name of the function, followed by a comma separated 
list of arguments within parentheses `()`

```python
def my_function(a, b, c)
```

This is known as a
[function signature](https://docs.python.org/3/library/functions.html#sorted).


## Implementing a function

The function's implementation should exist within an indented block directly 
below the function signature. You must append a colon `:` to the end of the 
function signature

```python
def function(a, b, c):
    print('a is', a)
    print('b is', b)
    print('c is', c)
```

Now you can invoke this function like any other function from the standard 
libary

```python
function(1, 2, 3)
```

This will print the following text to the console

```text
a is 1
b is 2
c is 3
```

### defining keyword arguments

Positional arguments are always declared first in a function signature. These 
arguments will be _required_ to invoke the function. If you'd like to define 
any _optional_ arguments, those must be declared _after_ the positional 
arguments using the `keyword=default` syntax

```python
def function(a, b=8, c=16):
    print('a is', a)
    print('b is', b)
    print('c is', c)
```

Given the function definition above, `a` is required, `b` is optional (with a 
default value `8`), and `c` is optional (with a default value `16`). When 
calling this function, if you wish to override any of these optional keyword 
arguments, you can refer to them by keyword

```python
function(1, c=3)
```

This would print the following text to the console

```text
a is 1
b is 8
c is 3
```

## Returning values

Often times you will want your function to manipulate some input data and
return a computed result. This is accomplished using a `return` statement

```python
def function(a, b, c):
    return (a + b) / c
```

If your function has a return value, you can store that value within a variable 
using the assignment operator `=`

```python
result = function(1, 2, 3)
```

