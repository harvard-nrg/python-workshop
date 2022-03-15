# Print and string formatting

One of the most tried and true debugging tools is
[`print`](https://docs.python.org/3/library/functions.html#print).

!!! attention ""
    Make liberal use of `print` to output text from your programs that 
    would be useful for troubleshooting and monitoring progress.

## Simple use case

You can pass any value to `print` that can be represented as a string

!!! note ""
    Most types of data in Python can be represented as a string.

```python
print('Hello, World!')
print(1)
print(3.14)
print(True)
print(None)
print([ 1, 2, 3 ])
```

## String formatting

_Format strings_ allow you to create more complex strings containing plain text 
and existing variables.

!!! tip "Read the documentation"
    String formatting is a whole
    [mini-language](https://docs.python.org/3.4/library/string.html#format-specification-mini-language) 
    within the Python language itself. I suggest referring to the 
    [official documentation](https://docs.python.org/3.4/library/string.html#format-string-syntax) 
    for more.

### Basic example

You define a format string like a any other string, except you must prefix the 
string with a `f`. Within the format string, you can use curly braces `{}` 
to reference a variable

```python
a = 'World'
print(f'Hello, {a}!')
```

In this example, Python will substitute the placeholder `{a}` with the value 
from the variable `a` which will result in the string `Hello, World!`.

### Real world example

Format strings are sometimes used to dynamically build shell commands. For example

```python
files = [
    ['subject_a.dcm', 'subject_a.nii.gz'],
    ['subject_b.dcm', 'subject_b.nii.gz'],
    ['subject_c.dcm', 'subject_c.nii.gz']
]

for infile, outfile in files:
    command = f'mri_convert {infile} {outfile}'
    print(command)
```

This will print the following shell commands 

```text
mri_convert subject_a.dcm subject_a.nii.gz
mri_convert subject_b.dcm subject_b.nii.gz
mri_convert subject_c.dcm subject_c.nii.gz
```

### Rounding `floats`

It's common for a developer to specify how a `float` value should be displayed 
within a formatted string. To do this, you can add a format specifier to your 
placeholder using `{variable:specifier}` syntax.

For example, if you want your format string to round the variable `pi` to 4 
decimal places, you would append `0.4f` to `pi`

```python
pi = 3.1415926
print(f'π rounded to 4 decimal places is {pi:0.4f}')
```

For more information on format specifiers, refer to the official documentation 
[here](https://docs.python.org/3.4/library/string.html#format-specification-mini-language).

