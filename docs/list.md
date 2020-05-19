# Data structures

Moving forward, there will be many instances where you need a variable to hold 
multiple related values. For this, you'll want to be confident using 
_data structures_.

## Lists

Lists start and end with square square brackets `[]` and items are separated 
with commas. Spaces don't matter

```python
a = [ 1, 2, 3, 4 ]
```

!!! question "Do I need to specify the size of the list in advance"
    Nope. Since Python is interpreted and 
    [garbage collected](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)) 
    you do not need to allocate memory, free memory, or declare the size 
    of your list in advance. Lists can even grow and shrink arbitrarily.
 
Of course we can store more than just integers in a list. Here's a list 
containing two strings

```python
a = [ 'Hello', 'World!' ]
```

We can also store a combination of data types within a list, including 
_another list_

!!! info "Split up long lines"
    In the example below, I've defined a list with each item on a separate 
    line. This is purely for the sake of readability. I'll often split up 
    [really long lines](https://en.wikipedia.org/wiki/Characters_per_line#In_programming)
    if I feel like things are getting out of hand.

```python
a = [
  1.0,
  'Hello, World!',
  [ 5.0, True, None ]
]
```

## Indexing

Retrieving items that you've added to a list is called _indexing_ or 
_subscripting_. Let's start with the list shown earlier

```python
a = [
  1.0,
  'Hello, World!',
  [ 5.0, True, None ]
]
```

The list _indexes_ are as follows
  
| index |      value            | type    |
|-------|-----------------------|---------|
|  0    | `1.0`                 | `float` |
|  1    | `'Hello, World!'`     | `str`   |
|  2    | `[ 5.0, True, None ]` | `list`  |

In Python, list indexes always start from 0 and increment to the length of the 
list minus 1. Let's retrieve a few items from the list above to prove to 
ourselves that list indexing works

```python
a[0]
a[1]
a[2]
```

Spoiler alert. It works.

## Insert

It's simple to add, remove, and replace elements within a list. Let's begin 
with list `insertion`. There are a few ways to insert an item into a list, but 
a common technique is to use the `insert` method. This method accepts two 
arguments. The first argument is a list index and the second argument is 
the value to insert at that index 

```python
a.insert(0, 'foobar')
```

This will insert the string `foobar` at index `0`, pushing all remaining items 
forward.

## Update

To update the value at a particular list index, using the assignment operator

```python
a[1] = 999
```

This will replace the value at index `1` with the integer `999`.

## Delete

Deleting an item involves slightly different syntax. You have to use a `del` 
statement

```python
del a[1]
```

This will delete the value at index `1` and shift all subsequent items backward. 

!!! note "Read the documentation"
    There are so many more list operations that go way beyond the ones 
    demonstrated here. It's worth looking over the official documentation
    [here](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

## Length

To get the length of a list, pass the list to the built-in `len()` function

```python
len(a)
```

This function will return an `int`.

## Exists

You can quickly check if a particular value exists within a list using an `in` 
statement

```python
20 in a
```

This will return a `bool`. We'll use `in` statements in later sections.

## Slicing

Slicing is a very powerful feature built into Python. If you've ever used 
Matlab, the syntax should be familiar. First, let's define a list containing 
the numbers `0` through `20`

```python
a = list(range(1, 21))
```

Slice syntax is defined as `start:end[:step]` where `step` is optional. If you 
want to retrieve the first 10 items, you would use the following syntax

```python
a[0:10]
```

If you omit the `start` index, it will default to zero

```python
a[:10]
```

If you want to get _every other_ item, add a colon `:` and specify a `step` 
value. By default, the `step` is 1, but here we'll set it to 2

```python
a[:20:2]
```

If you don't know the length of the list, just omit the `end` index which 
will default to the length of the list

```python
a[::2]
```

!!! note ""
    For more advanced information, visit the official documentation 
    [here](https://docs.python.org/3/library/functions.html#slice)

## Exercises

!!! tip "Exercise 1"
    Both `str` and `list` are considered 
    [_iterables_](https://docs.python.org/3/glossary.html#term-iterable) 
    in Python. Due to this, some operations you can perform on a `list` you can 
    also perform on a `str`, such as indexing and slicing. Give this a try.
