# Control flow

## The `for` loop

A `for` loop allows the same block of code to be executed multiple times. The 
general format of a `for` loop is as follows

```python
for item in iterable:
    code to be executed
```

## Iteration

Many of the data structures that we've encountered are 
[iterable](https://docs.python.org/3/glossary.html#term-iterable).
Suppose we have a `list` of scan information. Each item in the `list` is a 
`dict` containing various scan properties

```python
scans = [
    {
        'num': 1,
        'type': 'LOCALIZER',
    },
    {
        'num': 2,
        'type': 'MEMPRAGE'
    },
    {
        'num': 3,
        'type': 'BOLD'
    },
    {
        'num': 4,
        'type': 'BOLD'
    }
]
```

If you want to retrieve the scan numbers for all `BOLD` scans, you could use a 
`for` loop to iterate over the `scans` list and call the same block of code to 
populate a `numbers` list

```python
numbers = []

for scan in scans:
    if scan['type'] == 'BOLD':
        numbers.append(scan['num'])

print(numbers)
```

## Iterating over a `dict`

It's also possible to iterate over a `dict`, but there are some slight 
differences. By default, when you iterate over a `dict` you'll only receive 
its keys. For example

```python
a = {
    'key1': 1,
    'key2': 2,
    'key3': 3
}

for key in a:
    value = a[key]
    print(value)
```

If you want to iterate over the `dict` returning `key` and `value` pairs, you 
can use the following syntax

```python
for key, value in a.items():
    print('key =', key, 'value =', value)
```

Note that the above `for` loop is using
[tuple unpacking](/tuple/#unpacking).
