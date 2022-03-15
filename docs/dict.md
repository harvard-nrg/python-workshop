# Data Structures

## Dictionaries

Dictionaries are data structures that allow you to define custom indexes or
_keys_.

!!! note ""
    In other languages, dictionaries are referred to as _hash maps_, _hash 
    tables_, or _associative arrays_.

Dictionaries begin and end with curly braces `{}` and each key/value pair 
is separated by a comma `,`. You define keys and their corresponding 
values separated by a colon `:`

```python
a = {
  'name': 'Guido van Rossum',
  'yob': 1956
}
```

## Indexing

You can index into a dictionary using the defined keys, which is often easier 
and more robust than having to remember numeric indexes 

```python
a['name']
a['yob']
```

## Insert 

Use the assignment operator `=` to insert new items into an existing dictionary 

```python
a['job title'] = 'BDFL'
```

## Update

Use the assignment operator `=` to update dictionary items

```python
a['job title'] = None
```

## Delete

Use the `del` keyword to delete items from a dictionary

```python
del a['job title']
```

