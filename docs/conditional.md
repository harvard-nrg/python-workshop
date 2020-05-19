# Control flow

When writing more sophisticated applications, you'll be faced with making 
programmatic decisions about which lines of code to execute next based on 
whether or not certain conditions have been met. 

## Comparison operators

Also referred to as _relational operators_, comparison operators are used to 
compare values and return a `bool`. Out of the box, Python recognizes the 
following comparison operators

| operator | description              |
|----------|--------------------------|
|   `<`    | less than                |
|   `>`    | greater than             |
|   `==`   | is equal to              |
|   `!=`   | is not equal to
|   `<=`   | less than or equal to    |
|   `>=`   | greater than or equal to |

Some examples include

```python
1 < 2
2 > 1
1 == 1
1 != 2
2 <= 3
3 >= 2
```

## Boolean operators

Also referred to as _logical operators_, boolean operators are typically used 
to create conjunctions

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

## Truthiness of values

An incredibly useful feature within Python is how some values can evaluate to 
a `bool` even though they aren't actually `bool` values. This is useful in many 
situations. For example, it's fairly common to execute a block of code if a 
list is empty. The long form way of doing this would be

```python
a = []

if len(a) == 0:
    print('the list is empty')
```

But this is so common that Python will evaluate an empty list to `False` if 
it's empty

```python
if not a:
    print('the list is empty')
```

Other values that evaluate to `False` include an empty string `''`, an empty 
dictionary `{}`, `0` (or `0.0`), an empty tuple `()`, and empty set `set()`, 
and `None`.

## Exercises

!!! tip "Exercise 1"
    I encourage you to play around with conditional operators. Specifically, 
    try comparing two strings with the less-than or greater-than operators. 

