# Data Structures

## Sets

Sets allow you to accumulate items without duplicates. A set begins and ends 
with curly braces `{}` and each item is separated by a comma. Spaces don't 
matter here

```python
a = { 1, 1, 2, 1, 2, 2 }
```

Even though we've added multiple instances of `1` and `2`, if you inspect this 
set you'll see that it only contains a single instance of `1` and `2`.

## Alternate syntax

You may recall that curly braces are also used for dictionaries. This creates 
ambiguity when creating an empty set. If you use empty curly braces `{}`, you 
will create an empty `dict`. To create an empty `set`, you must use the `set()` 
function without any arguments
    
```python
a = set()
```

!!! attention "Python 2"
    The curly brace syntax for defining a `set` wasn't introduced to the 
    language until Python 2.7. To initialize a `set` with values you had 
    to use the `set()` function supplying your values as a `list`

    ```python
    a = set([ 1, 1, 2, 1, 2, 2 ])
    ```

## Set operations

Sets support some familiar set operations as well. For example, you can find 
the `union`, `intersection`, and `difference` between sets using the following 
methods

```python
a = { 1, 2, 3, 4, 5 }
b = { 1, 5, 6, 7, 8 }
a.intersection(b)       # intersection
a.difference(b)         # difference
a.union(b)              # union
```

## Adding and removing items

You can add and remove items from a `set` using the `add` and `remove` 
methods

```python
a.add(10)
a.remove(2)
```

Unfortunately, sets do not support indexing.

