# Importing and using modules
The following section will explore how to tap into the rest of the Python
[standard library](https://docs.python.org/3/library/index.html) 
by way of
[importing](https://docs.python.org/3/reference/simple_stmts.html#the-import-statement)
modules.

## The `os` module
The 
[`os`](https://docs.python.org/3/library/os.html)
module provides functions that allow you to interact with the operating 
system. To begin using functions from `os`, you first need to import it

```python
import os
```

### Joining paths
[`os.path.join`](https://docs.python.org/3/library/os.path.html#os.path.join)
allows you to combine strings with the appropriate
[path separator](https://docs.python.org/3/library/os.html#os.sep)

```python
os.path.join('/path/to/data/', 'sub-001', 'ses-001')
```

This function call will return the path `/path/to/data/sub-001/ses-001`.

### Listing a directory
[`os.listdir`](https://docs.python.org/3/library/os.html#os.listdir)
will list directory contents, similar to the `ls` utility from 
[GNU coreutils](https://www.gnu.org/software/coreutils/)

```python
for entry in os.listdir('.'):
    print(entry)
```

### Walking a directory 
If you want to crawl over a directory and every subdirectory from the command 
line, you would run a command like `ls -R` or `find`. In Python, you can use
[`os.walk`](https://docs.python.org/3/library/os.html#os.walk)

```python
for root, dirs, files in os.walk('.'):
    for file in files:
        fullfile = os.path.join(root, file)
        print(fullfile)
```

### Table of shell commands
Here's a quick list of commonly used Python functions and their corresponding 
GNU/Linux commands

| Linux command | Python function |
|---------------|-----------------|
| `cd`          | `os.chdir`      |
| `pwd`         | `os.getcwd`     |
| `chmod`       | `os.chmod`      |
| `chown`       | `os.chown`      |
| `rm`          | `os.remove`     |
| `mv`          | `os.rename`     |

## The `shutil` module
Similar to the `os` module, 
[`shutil`](https://docs.python.org/3/library/shutil.html)
contains more high-level functions for interacting with files and
directories

```python
import shutil
```

### Copying a file
To copy a file, you should use 
[`shutil.copy2`](https://docs.python.org/3/library/shutil.html#shutil.copy2). 
This function accepts the _source_ and _destination_ files

```python
shutil.copy2('/path/source.txt', '/path/destination.txt')
```

!!! tip ""
    Python contains several functions for copying a file. There's
    [`copy`](https://docs.python.org/3/library/shutil.html#shutil.copy),
    [`copyfile`](https://docs.python.org/3/library/shutil.html#shutil.copyfile), 
    and
    [`copy2`](https://docs.python.org/3/library/shutil.html#shutil.copy).
    `copy2` may be preferred under most circumstances since it preserves file 
    metadata. 

### Copying a directory
To copy an entire directory tree, you would typically use the `cp -R` commnad. In 
Python, you can use 
[`shutil.copytree`](https://docs.python.org/3/library/shutil.html#shutil.copytree).
This function accepts the _source_ and _destination_ directories

```python
shutil.copytree('/path/source', '/path/destination')
```

### Deleting a directory
To delete an entire directory from the command line, you would typically use 
`rm -r` and say a prayer. In Python, you would use 
[`shutil.rmtree`](https://docs.python.org/3/library/shutil.html#shutil.rmtree).
This function accepts the directory to delete

!!! danger "Destructive command"
    You will not be asked for confirmation. Use at your own risk.

```python
shutil.rmtree('/be/careful')
```

## `from x import y`
Instead of importing a module and calling a function

```python
import os

os.listdir()
```

you can use a `from` statement to import _only_ the function you need

```python
from os import listdir

listdir()
```

