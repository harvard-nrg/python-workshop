# Print and string formatting

One of the most powerful debugging tools you will ever encounter in this life 
is the
[`print`](https://docs.python.org/3/library/functions.html#print)
function. By default, this function will print text to 
[standard output](https://en.wikipedia.org/wiki/Standard_streams).

!!! attention "Logging is your friend"
    You can (and should) use `print` to emit text that would be useful for an 
    end user, to monitor the progress of your application, and to assist with 
    troubleshooting issues.

## Simple use case

The simplest use case is to print any value that can be represented as a 
string, which would be most types in Python. Obviously a `str` would work

```python
print('Hello, World!')
```

But you can also print an `int` , `float`, `bool`, `None`, and most if not 
all data structures

```python
print(1)
print(3.14)
print(True)
print(None)
print([ 1, 2, 3 ])
```

## String interpolation

Often times you will want to print more than just a single variable. To print a 
combination of text _and_ variables, the easiest way is to separate the text 
and variables using commas

```python
symbol = 'pi'
value = 3.1415

print(symbol, 'is approximately', value)
```

This would print the following message to the console

```text
pi is approximately 3.1415
```

## String formatting

String formatting is a more powerful way to concatenate text and variables.

!!! tip "Read the documentation"
    String formatting is nothing short of a
    [mini-language](https://docs.python.org/3.4/library/string.html#format-specification-mini-language) 
    within the Python language itself. Rather than trying to cover _everything_ 
    you can do with string formatting, I'll suggest that you refer to the 
    official documentation 
    [here](https://docs.python.org/3.4/library/string.html#format-string-syntax). 

### Basic example

To get started, we need to define a _format string_. This should look no 
different from a regular `str`, except for the embedded placeholders `{}`

```python
formatter = '{} is approximately {}'
```

When we call the `formatter.format()` method with the following positional 
arguments 

```python
a = 'pi'
b = 3.1415

formatter.format(a, b)
```

this produces the new `str`

```text
pi is approximately 3.1415
```

The placeholders `{}` were replaced with the arguments passed into the 
`formatter.format()` method. The first instance of `{}` was be replaced with 
the string `pi`, the second instance of `{}` was replaced with the value 
`3.1415`, and so on.

### Real world example

String formatting is commonly used to dynamically build commands that you want  
to run using the 
[`subprocess`](/subprocess)
module. For example

```python
input_file = 'file.dcm'
output_file = 'file.nii.gz'

formatter = 'mri_convert {} {}'

command = formatter.format(input_file, output_file)
```

### Rounding `floats`

Since rounding a `float` within a formatted string is so common, we'll cover 
that use case here. If you've ever used `sprintf` in other languages, the idea 
should be familiar. Within the `{}` placeholder, you can insert a format 
specification. For example, `{:0.4f}` will tell the string formatter to round 
the incoming `float` value to 4 decimal places

```python
formatter = '{:0.4f}'
formatted = formatter.format(3.1415926)
print('pi is approximately', formatted)
```

For more information about format specifiers, please refer to the official 
documentation 
[here](https://docs.python.org/3.4/library/string.html#format-specification-mini-language).

## Alternate syntax

You will almost certainly encounter the following syntax for string formatting 
in other peoples' code
    
```python
>>> '%0.4f' % 3.1415926
3.1416
```

While this is still valid Python syntax, the `.format` method shown above is 
the preferred approach.

