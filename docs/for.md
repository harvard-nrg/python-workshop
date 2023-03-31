# Control flow

## The `for` loop
A `for` loop allows the same block of code to be executed multiple times

```python
for item in iterable:
    code to be executed
```

## Iteration
Many of the data structures we've reviewed are defined as
[iterables](https://docs.python.org/3/glossary.html#term-iterable)
in Python. Suppose we have a list of scan information where each item in the 
list contains a `dict` of scan properties

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
`for` loop to iterate over `scans` and call the same block of code to populate 
a list of scan numbers

```python
numbers = []

for scan in scans:
    if scan['type'] == 'BOLD':
        numbers.append(scan['num'])

print(numbers)
```

This will print the result `[3, 4]`.

## Iterating over a dictionary
It's also common to iterate over a `dict`, however there are some subtle
differences. By default, when you iterate over a `dict` you'll only receive 
its keys

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

If you want to iterate over the `dict` returning both the `key` and `value` 
as a pair, you would use the following syntax

```python
for key,value in a.items():
    print('key =', key, 'value =', value)
```

The `.items()` method on a dictionary will return all key/value pairs as a 
list of tuples. The `for` loop shown above is
[unpacking](/tuple/#unpacking)
each tuple into the separate variables for `key` and `value`.
