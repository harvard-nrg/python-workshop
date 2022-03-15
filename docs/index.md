# Welcome to Python for Neuroimaging!

## A brief history

[Python](https://www.python.org) 
is a high-level,
[interpreted language](https://en.wikipedia.org/wiki/Interpreted_language)
created by 
[Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum). 

### 2 to 3

Python has undergone three major revisions since it's initial release back in 
1991. The most recent revision was Python 2 to 3. Python 2 still exists, but 
was
[officially deprecated](https://www.python.org/doc/sunset-python-2/)
on January 1st, 2020.

## The interpreter

Instead of having to
[compile](https://en.wikipedia.org/wiki/Compiled_language) 
source code into 
[machine code](https://en.wikipedia.org/wiki/Machine_code),
Python executes your code
one line at a time using an 
[_interpreter_](https://en.wikipedia.org/wiki/Interpreter_(computing)).

### starting the interpreter

Python should be installed by default on most Linux and macOS systems. To start 
the interpreter, simply open a terminal and type `python` or `python3` at the 
command prompt and hit <kbd>Enter</kbd>

```text
% python
Python 3.8.2 (default, Mar 26 2020, 15:43:04) 
[Clang 11.0.3 (clang-1103.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

!!! attention "Command not found"
    If you receive a `command not found` error, either your system does 
    not have Python installed, or your environment is misconfigured. Try
    logging into a FASSE host and use one of the existing Python modules
    
    ```bash
    module load ncf
    module load miniconda3/py39_4.11.0-ncf
    ```

    If that doesn't work, 
    [contact a system administrator](https://www.rc.fas.harvard.edu/about/contact/).
    
### executing statements

You can execute statements interactively by typing a statement at the prompt 
`>>>` and pressing <kbd>Enter</kbd>

```python
>>> 1 + 1
2
>>>
```

Python will read the input statement, evaluate it, print the result, and loop 
back to the command prompt. This is known as a 
[read-evaluate-print-loop](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)
or REPL.

### comments

Comments begin with a hash `#` and will be ignored

```python
>>> # this is a comment
```

For multi-line comments, you can use multiple hash `#` characters or triple 
quotation marks (single or double quotes work)

```python
"""
I am
a multiline
comment
"""
```

### quitting

To quit the Python interpreter, type <kbd>Control</kbd> + 
<kbd>D</kbd> or execute the `quit()` or `exit()` functions

```bash
>>> quit()
```

