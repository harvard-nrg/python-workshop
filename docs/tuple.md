# Data Structures

## Tuples

Tuples are effectively an
[immutable](https://en.wikipedia.org/wiki/Immutable_object)
list. Once a tuple has been defined, you cannot add, update, or delete items 
from it. A tuple begins and ends with parentheses `()` and items are separated 
by a comma `,`

!!! note ""
    Spaces don't matter here.

```python
a = ( 1, 2, 3 )
```

## Indexing

Like other 
[iterable](https://docs.python.org/3/glossary.html#term-iterable)
types in Python, you can index and
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
loops, you can _unpack_ a tuple into individual variables

```python
a, b, c = ( 1, 2, 3 )
```

In this case `a = 1`, `b = 2`, and `c = 3`. Remember this pattern as it often 
appears in code and documentation.

## Immutability

The immutability property of a tuple is desirable under some 
circumstances. For example, only immutable types in Python can be 
[hashed](https://en.wikipedia.org/wiki/Hash_function)
and only hashable types can be used as dictionary keys. For example,
this is perfectly legal code

```python
a = {
    ( 'StudyA', 'Subject1' ): [ 'Session1', 'Session2' ],
    ( 'StudyA', 'Subject2' ): [ 'Session3', 'Session4' ],
    ( 'StudyB', 'Subject1' ): [ 'Session5', 'Session6' ]
}
```

!!! note ""
    Note that you cannot hash a tuple if it contains a mutable type.

and subsequently you can retrieve an item from this dictionary using 
`('StudyA','Subject2')`

```python
a[( 'StudyA', 'Subject2' )]
```
