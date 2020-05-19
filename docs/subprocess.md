# Subprocesses

Many neuroimaging tools are implemented as single command line tools that 
[do a thing](https://en.wikipedia.org/wiki/Unix_philosophy).
To build more complex analysis streams, you will inevitably have to chain 
together several command line tools to build what's known as a 
[pipeline](https://en.wikipedia.org/wiki/Pipeline_(computing)).
Python has very mature support for running subprocesses, some of which will 
be demonstrated here.

## The `subprocess` module

Running commands from the command line is commonly referred to as running a 
[_subprocess_](https://en.wikipedia.org/wiki/Child_process).
Running subprocesses in Python is achieved using the 
[`subprocess`](https://docs.python.org/3/library/subprocess.html) module

```python
import subprocess
```

## Running a subprocess

A very simple way to run a subprocess is by way of the 
[`subprocess.check_output()`](https://docs.python.org/3/library/shutil.html#shutil.rmtree)
function. The first argument should be your command (as a `str`) and the second 
argument should be `shell=True` which tells `subprocess` to run your command 
within a subshell.

In the example below, we'll run the command `ls -la`, capture the console output 
into a variable named `output`, and print that output to the screen

```python
output = subprocess.check_output('ls -la', shell=True)

print(output.decode())
```

!!! question "What's `string.decode()`"
    Console output can be in any
    [character encoding](https://en.wikipedia.org/wiki/Character_encoding). 
    Since Python
    [<strike>can't</strike>](https://github.com/chardet/chardet) 
    doesn't automatically detect what encoding your string is in, you must 
    call the `decode()` method, which defaults to `utf-8`.

## Handling errors

If a subprocess fails, you'll receive a 
[`subprocess.CalledProcessError`](https://docs.python.org/3/library/subprocess.html#subprocess.CalledProcessError).
An _uncaught_ exception like this will usually crash your program. But if you want 
to catch the error and handle it (perhaps by ignoring it), you can encapsulate 
your the function call in a 
[`try statement`](https://docs.python.org/3/reference/compound_stmts.html#try)

```python
try:
    output = subprocess.check_output('ls -z', shell=True)
except subprocess.CalledProcessError as e:
    print(e.returncode)
```
