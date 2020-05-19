# Writing command line tools

We've covered a lot of ground. Now that we have a handle on the Python 
interpreter and some fundamental Python syntax, we can take the commands we've 
been plugging into the interpreter and create a command line application.

## Basic example

To begin, open a new file named `hello.py` and enter the following contents

```python
#!/usr/bin/env python

print('Hello, World!')
```

Save the file and make it executable using the following _shell_ command

```bash
% chmod u+x hello.py
```

Now you can execute your script from the command line

```bash
% ./hello.py
Hello, World!
```

## Real world example

Let's take a look at a real-world example. The command line application shown 
below will use the
[`yaxil`](https://yaxil.readthedocs.io/en/latest/)
package to query a public data set on `central.xnat.org`, retrieve all of the
scan numbers, and download those scans into a directory named `./xnat-data`

```python
#!/usr/bin/env python
  
import yaxil

xnat = 'central-xnat'
project = 'CENTRAL_OASIS_LONG'
label = 'OAS2_0001_MR2'
out_dir = './xnat-data'

auth = yaxil.auth(xnat)

scan_ids = []
for scan in yaxil.scans(auth, label, project=project):
    scan_id = scan['id']
    scan_ids.append(scan_id)

yaxil.download(auth, label, scan_ids, out_dir=out_dir)
```

The only shortcoming is that the variables `xnat`, `project`, `label`, and 
`out_dir` are baked into the application. The next section will show you how 
to turn these into _command line arguments_.

## Command line arguments

Suppose that you wrote a XNAT downloader script, named `downloader.py`, that 
you wanted to accept `xnat`, `project`, `label`, and `out_dir` on the command 
line

```bash
% ./downloader.py --xnat central-xnat --project CENTRAL_OASIS_LONG --label OAS2_0001_MR2 --out-dir ./xnat-data
```

You can certainly access the raw command line arguments by importing the `sys` 
module and sifting through `sys.argv`

```python
import sys

print(sys.argv)
```

But that's going to be a lot of work to parse. Fortunately, there's a much 
cleaner way to define and parse command line arguments using one of my favorite 
modules, 
[`argparse`](https://docs.python.org/3/library/argparse.html).

!!! tip "Read the docs"
    The `argparse` module is truly brilliant. The functionality demonstrated 
    here does not do it justice. I highly recommend that you take the time to 
    browse the official documentation 
    [here](https://docs.python.org/3/library/argparse.html).

### defining

First, import the `argparse` module and create an 
[`argparse.ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser) 
object

```python
import argparse

parser = argparse.ArgumentParser()
```

Now, add your arguments to the `parser` object by calling 
[`parser.add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument)

```python
parser = argparse.ArgumentParser()
parser.add_argument('--xnat')
parser.add_argument('--project')
parser.add_argument('--label')
parser.add_argument('--out-dir')
```

### parsing

Now you can call
[`parser.parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args)
to parse the user supplied command line arguments

```python
args = parser.parse_args()
```

To access each argument, take the argument name, remove any leading dashes `-`, 
replace any embedded dashes `-` with an underscore `_`, and you should be able 
to access that property on the `args` object

```python
print('xnat is', args.xnat)
print('project is', args.project)
print('label is', args.label)
print('out_dir is', args.out_dir)
```

## Exercises

!!! tip "Exercise 1"
    Try adding command line arguments to the
    [real world example](#real-world-example).
