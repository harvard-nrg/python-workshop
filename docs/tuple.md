# Data Structures

## Tuples

Tuples are similar lists in some ways, except that they cannot be changed after 
they are created. In other words, they're 
[immutable](https://en.wikipedia.org/wiki/Immutable_object).
A tuple begins and ends with parentheses `()` and items are separated by 
commas. Spaces don't matter

```python
a = ( 1, 2, 3 )
```

## Indexing

Like many other 
[iterables](https://docs.python.org/3/glossary.html#term-iterable)
we've encountered, you can index and
[slice](https://docs.python.org/3/library/functions.html#slice)
tuples

```python
a[0]
a[1]
a[::2]
```

## Unpacking

Often used in
[`for`](/for)
loops, you can _unpack_ a tuple into individual variables using the following 
syntax

```python
a, b, c = ( 1, 2, 3 )
```

In this case `a` would be equal to `1`, `b` equal to `2`, and `c` equal to `3`.

## Immutability

The immutability property of tuples is needed in some situations. For example, 
only immutable types in Python can be 
[hashed](https://en.wikipedia.org/wiki/Hash_function) 
and only hashable types can be used as dictionary keys. In other words, you can 
do this

```python
a = {
    ( 'StudyA', 'Subject1' ): [ 'Session1', 'Session2' ],
    ( 'StudyA', 'Subject2' ): [ 'Session3', 'Session4' ],
    ( 'StudyB', 'Subject1' ): [ 'Session5', 'Session6' ]
}
```

Now you can retrieve an item from this dictionary using `( 'StudyA', 'Subject2' )` 
as opposed to maintaining a second lookup table

```python
a[( 'StudyA', 'Subject2' )]
```

