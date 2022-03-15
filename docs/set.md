# Data Structures

## Sets

Sets allow you to accumulate items without duplicates. A set begins and ends 
with curly braces `{}` and each item is separated by a comma `,`

!!! note ""
    Spaces don't matter here.

```python
a = { 1, 1, 2, 1, 2, 2 }
```

Note that even though we've added multiple instances of `1` and `2`, the set 
object only contains a single instance of `1` and `2`.

```python
>>> print(a)
{1, 2}
```

## Alternate syntax

Unfortunately, Python also uses curly braces `{}` to define sets _and_ 
dictionaries. The following will create an empty dictionary

```python
a = {}
```

To create an empty set, you need to use the 
[`set()`](https://docs.python.org/3/library/functions.html#func-set)
function without any arguments
    
```python
a = set()
```

## Set operations

The set data type supports many conventional set operations. You can find the 
`union`, `intersection`, and `difference` between two sets using the following 
methods

```python
a = { 1, 2, 3, 4, 5 }
b = { 1, 5, 6, 7, 8 }
a.intersection(b)       # intersection
a.difference(b)         # difference
a.union(b)              # union
```

## Adding and removing items

You can add and remove items from a set using the `add` and `remove` 
methods

```python
a.add(10)
a.remove(2)
```

## Indexing

Sets, which are inherently unordered collections, do not support indexing.

