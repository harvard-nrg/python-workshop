# Control flow

## Comparison operators

Python provides all of the conventional _relational operators_ to compare two 
values

| operator | description              |
|----------|--------------------------|
|   `<`    | less than                |
|   `>`    | greater than             |
|   `==`   | is equal to              |
|   `!=`   | is not equal to
|   `<=`   | less than or equal to    |
|   `>=`   | greater than or equal to |

Examples include

```python
1 < 2
2 > 1
1 == 1
1 != 2
2 <= 3
3 >= 2
```

These will return a `bool` result.

## Boolean operators

Also referred to as _logical operators_, boolean operators are used to create 
_conjunctions_

| operator | desription  | logic symbol |
|----------|-------------|--------------|
|   `and`  | logical and | `p ∧ q`      |
|   `or`   | logical or  | `p ∨ q`      |
|   `not`  | logical not | `¬p`         |

Some examples include

```python
2 > 1 and 2 < 3
True or False
True and not False
```

These will return a `bool` result.

## Truthiness of values

Python will interpret empty values as `False` and non-empty values as `True`. 
For example, it's common to execute a block of code if a `list` is empty. One 
way to do this would be

```python
a = []

if len(a) == 0:
    print('the list is empty')
```

However, since Python will interpret an empty list as `False` you can do the 
following instead

```python
if not a:
    print('the list is empty')
```

Other values that evaluate to `False` include an empty string `''`, an empty 
dictionary `{}`, the integer value `0`, the float value `0.0`, an empty tuple 
`()`, an empty set `set()`, and `None`.

## Exercises

!!! tip "Exercise 1"
    Play around with conditional operators. Specifically, you should try 
    comparing two strings with the less-than or greater-than operators. 

