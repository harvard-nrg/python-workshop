# Variables, assignment, and types

This may seem a bit elementary, but let's review how to define variables and go 
over the various 
[_primitive types_](https://en.wikipedia.org/wiki/Language_primitive)
in Python.

## Defining a variable

Enter the following statement at the Python command prompt `>>>` to define the 
variable `pi`

```python
pi = 3.1415
```

!!! note ""
    Note that you do not need to use `let`, `var`, or provide any type hinting 
    keywords before a variable declaration. You also don't need a semicolon 
    at the end of each statement.

### defining a variable from an expression

The right side of a variable assignment does not need to be a static value. It 
can be an expression

```python
a = 1 + 1
```

Python will evaluate the right side of the assignment operator and send the 
result to the left. This left-right associative property allows you to use an 
existing variable to redefine itself

```python
a = a + 1
```

## Primitive types

Python includes several low-level _primitive_ data types such as integers 
`int`, decimals `float`, strings `str`, booleans `bool`, and null `None`

```python
a = 1                               # int
b = 3.14                            # float
c = "I'm a double quoted string"    # str
d = 'I\'m a single quoted string'   # str
e = True                            # bool
f = False                           # bool
g = None                            # None
```

!!! question "Should I define strings use single or double quotes"
    Using single or double quotes is mostly a stylistic choice. However, if 
    you intend to use a single quote within a single-quoted string, or a 
    double quote within a double-quoted string, you'll need to escape the 
    embedded quote with a backslash `\` character as shown above.

## Checking types

You can check the type of a variable or its 
[class](https://docs.python.org/3/tutorial/classes.html)
at any time by passing it to the built-in
[`type()`](https://docs.python.org/3/library/functions.html#type)
function.

```python
type(a)
```
