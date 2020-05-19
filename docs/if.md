# Control flow

## The `if` condition

The `if` statement allows you to decide whether or not to execute a block of 
code based on the outcome of a truth condition. The general syntax of an `if` 
statement is

```python
if condition:
  code to run if True
```

!!! warning "Indentation is critically important" 
    Python uses indentation to denote a block of code. Part of the reason is 
    to enforce consistent 
    [coding style](https://www.python.org/dev/peps/pep-0008/).
    A block of code is considered open on indent and closed on dedent. 

Let's look at the trivial example below. Because `a == 10` returns `True`, the 
indented block of code will be executed

```python
a = 10

if a == 10:
  print('condition is True')
```

## The `else` clause

If you want to run a different block of code if the evaluated condition returns 
`False`, you can add an `else` clause

```python
if a == 0:
  print('condition is True')
else:
  print('condition is False')
```

## The `elif` clause

We can further complicate this `if` statement by adding an `elif` clause, 
which is short for "else if"

```python
if a == 0:
  print('a is equal to 0')
elif a == 10:
  print('a is equal to 10')
else:
  print('a is not equal to 0 or 10')
```
