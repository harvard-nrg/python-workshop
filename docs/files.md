# Reading and writing files

## Reading a file
To read a file, open the file using the built-in 
[`open()`](https://docs.python.org/3/library/functions.html#open)
function and call the
[`.read()`](https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects)
method on the resulting file object

```python
fo = open('file.txt')

content = fo.read()
```

To close the file, call the `.close()` method

```python
fo.close()
```

### character encoding
Calling `open()` on a file without any additional arguments will assume the 
file being opened is a text file containing a UTF-8 encoded string. If you 
know this is not the case, you are responsible for opening the file in 
_binary mode_ by passing `rb` as the mode

```python
fo = open('file.txt', 'rb')
```

Calling the `.read()` method on the resulting file object will yield a 
byte-string. To decode the byte-string, you must call `.decode()` with the 
correct character encoding as the first argument

```python
content = content.decode('UTF-8')
```

!!! tip ""
    UTF-8 is common, and backwards compatible with ASCII, but is 
    not the only character encoding.

## Writing a file
The process for writing a file is similar to reading. Simply open the file 
using the built-in `open()` function, however you need to open the file in 
_write mode_ by passing `w` as the second argument

```python
fo = open('file.txt', 'w')

fo.write('Hello, World!\n')
```

It's more important to call `.close()` after writing a file to ensure that 
the write buffer has been flushed

```python
fo.close()
```

## Appending to a file
Appending content to an existing file requires opening the file in 
_append mode_ by passing `a` as the second argument

```python
fo = open('file.txt', 'a')

fo.write(another line')

fo.close()
```

## File context manager
Forgetting to call `.close()` is a common mistake. Fortunately, the file 
object returned by `open()` supports the 
[context manager](https://docs.python.org/3/reference/datamodel.html#context-managers)
interface. To use a context manager, you wrap the function call in a 
[`with` statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)

```python
with open('file.txt', 'w') as fo:
    fo.write('Hello, World!\n')
```

The benefit is that as soon as you dedent from the `with` block, your file will 
be automatically closed. It's a good habit to use `with open`.

## CSV files
Let's take a moment to explore the
[`csv`](https://docs.python.org/3/library/csv.html)
module for reading a
[CSV](https://en.wikipedia.org/wiki/Comma-separated_values)
file. To begin, import the module

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

Open this CSV file using `open()` function, then pass the resulting file object 
to `csv.reader()`. This will return a CSV reader object

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
The first row of a CSV file usually contains column headers. It's useful to 
to combine each row with the column headers so that you can retrive items using 
dictionary-based indexing. The `csv.DictReader` can do this for you

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

