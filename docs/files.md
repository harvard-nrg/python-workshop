# Reading and writing files

## Reading a file

To read from file, simply open the file using the built-in 
[`open()`](https://docs.python.org/3/library/functions.html#open)
function and call `.read()` on the resulting file object

```python
fo = open('file.txt')

content = fo.read()
```

To close the file, call `close()` on the file object

```python
fo.close()
```

### character encoding

The result from calling `fo.read()` can sometimes yield a byte-string. Python 
will not automatically decode strings for you. To decode the result, you must 
know the character encoding and call the `.decode()` method. If the string is 
in `utf-8` for example, you would call

```python
content = content.decode('utf-8')
```

!!! tip ""
    UTF-8 is common but by no means the only character encoding.

## Writing a file

The process for writing a file is similar to reading. Again, you need to 
open the file using the built-in `open()` function, but this time you must 
open the file in write mode using `w` as the second positional argument

```python
fo = open('file.txt', 'w')

fo.write('Hello, World!\n')
```

It's more important to call `.close()` after writing to a file to ensure that 
the write buffer has been flushed to disk

```python
fo.close()
```

## Appending to a file

Similar to writing, appending content to an existing file requires opening the 
file in append mode using `a` as the second positional argument

```python
fo = open('file.txt', 'a')

fo.write(another line')

fo.close()
```

## File context manager

Forgetting to call `close()` is a common mistake. Fortunately, the file 
object returned by `open()` supports the 
[context manager](https://docs.python.org/3/reference/datamodel.html#context-managers)
interface. To use a context manager, you must wrap the function call in a 
[`with` statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)

```python
with open('file.txt', 'w') as fo:
    fo.write('Hello, World!\n')
```

The primary benefit is that as soon as you dedent the `with` block, the file 
will be closed.

## CSV files

Since reading 
[CSV](https://en.wikipedia.org/wiki/Comma-separated_values)
files is so common, we'll take some time to explore the 
[`csv`](https://docs.python.org/3/library/csv.html)
module.

To begin using the `csv` module, import it 

```python
import csv
```

### Reading CSV (basic)

Suppose this is the CSV file we're trying to read

```csv
Subject,Metric 1,Metric 2
Subject_001,1,1
Subject_002,2,0
Subject_003,3,1
```

We would open this CSV file using `open()` function, then pass the resulting 
file object to `csv.reader()`. This will return a CSV reader object

```python
fo = open('file.csv')

reader = csv.reader(fo)
```

Since an open CSV reader object is iterable, you can loop over it row-by-row 
using a `for` loop

```python
for row in reader:
    print(row)
```

This loop will print the following text to the console. As shown here, each row 
is parsed and returned as a `list`

```python
['Subject', 'Metric 1', 'Metric 2']
['Subject_001', '1', '1']
['Subject_002', '2', '0']
['Subject_003', '3', '1']
```

### Dictionary reader

The first row of a CSV file usually contains column headers. It's fairly common 
to combine each row with the column headers so that you can retrive items using 
`dict` indexing. Here's the long form version of this

!!! attention ""
    The example below is for illustrative purposes. There's a better way.

```python
fo = open('file.csv')
reader = csv.reader(fo)
headers = next(reader)              # get the first row
for row in reader:                  # iterate over the remaining rows 
    row = dict(zip(headers, row))   # combine headers and values
    print(row['Metric 1'])
```

You shouldn't bother with all of that. This is so common that the `csv` module 
includes a `csv.DictReader` to do it for you

```python
fo = open('file.csv')
reader = csv.DictReader(fo)
for row in reader:
    print(row['Metric 1'])
```

!!! tip "Pandas"
    You should also check out 
    [`pandas`](https://pandas.pydata.org/)
    which has even more advanced CSV parsing and querying capabilities.

