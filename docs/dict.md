# Data Structures

## Dictionaries

One limitation you'll encounter with the `list` data structure is that indexes 
must be numeric. If you want to build a list using a different type of data for 
each index, you'll need to use a dictionary or `dict`.

!!! note "Also known as"
    In other languages, dictionaries are referred to as _hash maps_, _hash 
    tables_ or _associative arrays_ and in Python the syntax closely resembles 
    [JSON](https://json.org).

Dictionaries start and end with curly braces `{}` and each item is separated 
by a comma. Unlike lists, you must define your own _keys_ (or indexes) and 
their corresponding values, separated by a colon. Here's a quick example

```python
a = {
  'name': 'Guido van Rossum',
  'yob': 1956
}
```

## Indexing

You can index into the dictionary shown above using the keys `name` and `yob` 
which is more intuitive than remembering numerical indexes

```python
a['name']
a['yob']
```

## Insert 

You can also insert an item into an existing dictionary using the assignment 
operator

```python
a['job title'] = 'BDFL'
```

## Update

You can update an existing dictionary item using the assignment operator

```python
a['job title'] = None
```

## Delete

Similar to lists, deleting an item requires the `del` statement

```python
del a['job title']
```

