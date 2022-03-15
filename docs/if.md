# Control flow

!!! warning "Indentation is important" 
    Python uses indentation or the 
    [off-side rule](https://en.wikipedia.org/wiki/Off-side_rule)
    to declare a _block_ of code. A
    [code block](https://en.wikipedia.org/wiki/Block_(programming))
    is considered _open_ on indent and _closed_ on dedent.

## The `if` condition

The general syntax of an `if` statement in Python is

```python
if condition:
  code to execute if True
```

In the example below, since `a == 10` evaluates to `True` the indented block 
of code will be executed

```python
a = 10

if a == 10:
  print('condition is True')
```

## The `else` clause

If you want to execute a different block of code if the evaluated condition 
returns `False`, you would use an `else` clause

```python
if a == 0:
  print('condition is True')
else:
  print('condition is False')
```

## The `elif` clause

We can further complicate this `if` statement with an `elif`, short for 
_else if_

```python
if a == 0:
  print('a is equal to 0')
elif a == 10:
  print('a is equal to 10')
else:
  print('a is not equal to 0 or 10')
```
