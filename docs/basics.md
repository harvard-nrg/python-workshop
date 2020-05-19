# Variables, assignment, and types

This may seem elementary for some, but let's quickly review how to define 
variables and some of the 
[_primitive_](https://en.wikipedia.org/wiki/Language_primitive)
types that exist in Python.

## Defining a variable

Enter the following statement at the Python command prompt `>>>` to define the 
variable `pi`

```python
pi = 3.1415
```

Note that you do not need to use `let`, `var`, or any other keywords before a 
variable declaration. You may also notice that there's no need for a semicolon 
at the end of each statement. Yay for conciseness. 👍

### from an expression

It's a little early to dive into expressions, but it is worth noting here that 
the right side of a variable assignment does not need to be a static value. It 
can be an expression

```python
a = 1 + 1
```

Python will evaluate the right-hand side of the assignment operator and send 
the result to the left. Given this left-to-right associative property, nothing 
would preclude you from using an existing variable to redefine itself

```python
a = a + 1
```

## Primitive types

By default, Python understands several low-level data types by default. The 
list includes integers (`int`), decimal numbers (`float`), strings (`str`), 
booleans (`bool`), and a special value for nothing (`None`). Here are some 
examples

```python
a = 1                               # int
b = 3.14                            # float
c = "I'm a doudble quoted string"   # str
d = 'I\'m a single quoted string'   # str
e = True                            # bool
f = False                           # bool
g = None                            # None
```

!!! question "Should I define strings use single or double quotes"
    Using single or double quotes is largely a stylistic choice. However, if 
    you're defining a string that must contain a single (or double) quote, you 
    should consider using double (or single) quotes. Alternatively, you can use 
    the back slash escape character `\` as demonstrated above.

## Checking types

We're seriously jumping ahead here now, but still worth mentioning that you can 
always check the type of a variable 
(or its [_class_](https://docs.python.org/3/tutorial/classes.html)) 
by passing it to the built-in
[`type()`](https://docs.python.org/3/library/functions.html#type)
function. This can come in handy

```python
type(a)
```
