# Importing and using modules

Up to this point, we've introduced various functions such as `len()`, `set()`, 
and `type()`. These are just a small number of the built-in
[functions](https://docs.python.org/3/library/functions.html) 
available to your application the moment you start Python. In the 
following section we'll explore how to tap into the rest of the 
[standard library](https://docs.python.org/3/library/index.html) 
by way of
[import](https://docs.python.org/3/reference/simple_stmts.html#the-import-statement)
statements.

## The `os` module

The 
[`os`](https://docs.python.org/3/library/os.html)
module provides functions that allow you to interact with the 
operating system. To use functions from the `os` module, import it

```python
import os
```

### Joining paths

You can easily combine strings with the appropriate
[path separator](https://docs.python.org/3/library/os.html#os.sep)
using
[`os.path.join()`](https://docs.python.org/3/library/os.path.html#os.path.join)

```python
os.path.join('/path/to/data/', 'sub-001', 'ses-001')
```

This function will return the path `/path/to/data/sub-001/ses-001`. Note that 
any redundant path separator characters `/` will be collapsed into a single 
character.

### Listing a directory

The `ls` command line utility from 
[GNU coreutils](https://www.gnu.org/software/coreutils/), 
will print directory entries to the console. 
This can also be achieved within Python using the 
[`os.listdir()`](https://docs.python.org/3/library/os.html#os.listdir)
function, which returns a `list` of files

```python
for entry in os.listdir('.'):
    print(entry)
```

### Walking a directory 

If you want to walk over a directory and each subdirectory from the command 
line, you would likely reach for a command like `ls -R` or `find`. In Python, 
you can do this with 
[`os.walk`](https://docs.python.org/3/library/os.html#os.walk)

```python
for root, dirs, files in os.walk('.'):
    for file in files:
        fullfile = os.path.join(root, file)
        print(fullfile)
```

The `os.walk()` function returns a 
[_generator_](https://docs.python.org/3/glossary.html#term-generator-iterator)
object. Generators are iterable and can be used with a `for` loop. On each 
iteration, you will recive a `tuple` containing the root directory, a list 
of directories, and a list of files. In the above example, we're using 
[tuple unpacking](../tuple/#unpacking) 
into the separate variables `root`, `dirs`, and `files`.

### Table of shell commands

Here's a quick list of commonly used Python functions and their corresponding 
Linux/UNIX commands

| Linux command | Python function |
|---------------|-----------------|
| `cd`          | `os.chdir`      |
| `pwd`         | `os.getcwd`     |
| `chmod`       | `os.chmod`      |
| `chown`       | `os.chown`      |
| `rm`          | `os.remove`     |
| `mv`          | `os.rename`     |

## The `shutil` module

While this is a little confusing, certain Linux commands have functional 
eqivalents in the `os` module while others are in the 
[`shutil`](https://docs.python.org/3/library/shutil.html)
module. To use functions from `shutil`, import the module

```python
import shutil
```

### Copying a file

To copy a file, you should use 
[`shutil.copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2). 
This function accepts arguments for the _source_ and _destination_ files

```python
shutil.copy2('/path/source.txt', '/path/destination.txt')
```

!!! tip "There's more than one way to copy a file"
    Python has multiple ways to copy a file. There's `copy()`, `copyfile()`, 
    `copyfileobj()`, and `copy2()`. I tend to use `copy2()` since this 
    function preserves file metadata. Frankly, I'm not sure under what 
    circumstances you would want any other behavior.

### Copying a directory

To copy an entire directory, you would typically use the `cp -R` commnad. In 
Python, you would use 
[`shutil.copytree()`](https://docs.python.org/3/library/shutil.html#shutil.copytree).
This function accepts two arguments for the _source_ and _destination_ 
directories

```python
shutil.copytree('/path/source', '/path/destination')
```

### Deleting a directory

To delete an entire directory from the command line, you would typically reach 
for the `rm -rf` command and say a quick prayer. In Python, you would use 
[`shutil.rmtree()`](https://docs.python.org/3/library/shutil.html#shutil.rmtree).
This function accepts the directory to delete as its first argument

!!! danger "Destructive command ahead"
    You will <u>not</u> be asked for confirmation. Use at your own risk.

```python
shutil.rmtree('/be/careful')
```

## `from x import y`

Instead of importing a module and calling a function like we've seen earlier

```python
import os

os.listdir()
```

you can use a `from` statement to import _only_ the function you intend to use

```python
from os import listdir

listdir()
```

