# Data structures

## Lists

Also known as _arrays_ in other languages, a `list` in Python begins and ends 
with square brackets `[]` and individual items are separated with a comma `,`

!!! note ""
    Spaces don't matter here.

```python
a = [ 1, 2, 3, 4 ]
```

!!! question "Do I need to specify the size of the list in advance"
    No. Since Python is interpreted and 
    [garbage collected](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)) 
    there's no need to explicitly allocate memory, free memory, or declare the 
    size of a `list` in advance.
 
You can store any type of data in a list

```python
a = [ 'Hello', 'World!' ]
```

You can even store multiple types of data, including other lists

```python
a = [
  1.0,
  'Hello, World!',
  [ 5.0, True, None ]
]
```

!!! info "Split up long lines"
    In the example below, you'll see a list printed with each item on a separate 
    line. It's considered good practice to
    [split lines at 80 characters](https://en.wikipedia.org/wiki/Characters_per_line#In_programming)
    for readability.

## Indexing

Retrieving items from a list is called _indexing_ or _subscripting_. Let's 
revisit the list from earlier

```python
a = [
  1.0,
  'Hello, World!',
  [ 5.0, True, None ]
]
```

The _indexes_ are as follows
  
| index |      value            | type    |
|-------|-----------------------|---------|
|  0    | `1.0`                 | `float` |
|  1    | `'Hello, World!'`     | `str`   |
|  2    | `[ 5.0, True, None ]` | `list`  |

In Python, list indexes start at `0` and increment to the length of the 
list minus `1`. Let's retrieve a few items

```python
a[0]
a[1]
a[2]
```

## Insert

Python has a few different ways to insert new items into an existing list. 
More commonly, you will use the
[`.insert()`](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
method. This method accepts two arguments. The first argument is a list 
index and the second argument is the value you want to insert at that index 

```python
a.insert(0, 'foobar')
```

This will insert the string `foobar` at index `0`, pushing all subsequent 
items forward.

## Update

Use the assignment operator `=` to update an item at a specific index

```python
a[1] = 999
```

This will replace the value at index `1` with the integer value `999`.

## Delete

Use the `del` keyword to delete an item from a list

```python
del a[1]
```

This will delete the value at index `1` and shift all subsequent items back. 

!!! note "Read the documentation"
    Refer to the official documentation
    [here](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
    for all available list operations.

## Length

To see the length of a list, pass it to the built-in
[`len()`](https://docs.python.org/3/library/functions.html#len)
function

```python
len(a)
```

This function will return an `int`.

## Exists

To check whether or not a specific value exists within a given list, use the 
`in` keyword

```python
20 in a
```

This statement will return a `bool`.

## Slicing

Slicing is a powerful feature built into Python. If you've ever used C or 
Matlab, the syntax should be familiar. Let's define a list containing the 
numbers `0` through `20` using the built-in
[`range()`](https://docs.python.org/3/library/stdtypes.html?highlight=range#ranges)
function

!!! note ""
    For `range()` to return all numbers from `1` to `20`, you have to specify 
    that you want numbers from `1` to `21`.

```python
a = list(range(1, 21))
```

Slice syntax is defined using `start:end[:step]` where `step` is optional. If 
you want to retrieve the first 10 items, you would specify the following slice

```python
a[0:10]
```

If you omit the `start` index, it will default to `0`

```python
a[:10]
```

Add a colon `:` and specify a step value of `2` to get _every other_ item

```python
a[:20:2]
```

If you don't know the length of the `list`, omit the `end` index to default to 
the maximum length

```python
a[::2]
```

!!! note ""
    For more advanced information, visit the official documentation 
    [here](https://docs.python.org/3/library/functions.html#slice)
