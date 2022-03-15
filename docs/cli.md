# Writing command line tools

To write a command line tool in Python, open a new plain text file named 
`hello.py` and enter the following contents

```python
#!/usr/bin/env python

print('Hello, World!')
```

Save the file and make it executable by executing the following shell command

```bash
% chmod u+x hello.py
```

Now you can execute your script from the command line

```bash
% ./hello.py
Hello, World!
```

## Command line arguments

Imagine that you want to write a script to download data from your local 
[XNAT](https://xnat.org)
installation. You'll need to accept the command line arguments `--hostname`, 
`--session`, and `--output-dir`

```bash
% ./download.py --hostname xnat.example.com  \
                --session LABEL \
                --output-dir ./output
```

Python includes a traditional C-style parser
[`getopt`](https://docs.python.org/3/library/getopt.html),
but there's a more convenient way to define and parse command line 
arguments using
[`argparse`](https://docs.python.org/3/library/argparse.html).

## argparse

### defining command line arguments

To define command line arguments, first import the `argparse` module and create 
an instance of 
[`argparse.ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser) 

```python
import argparse

parser = argparse.ArgumentParser()
```

Now, you can add your arguments to the `parser` object by calling 
[`parser.add_argument`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument)

```python
parser = argparse.ArgumentParser()
parser.add_argument('--hostname')
parser.add_argument('--project')
parser.add_argument('--label')
parser.add_argument('--output-dir')
```

### parsing the command line

To parse the command line arguments entered by the user, simply call
[`parser.parse_args`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args)

```python
args = parser.parse_args()
```

## accessing the command line arguments

Each command line argument is automatically converted into a property on the 
object returned by `parse_args()`. The name of the property is similar but 
not identical to the name of the argument that was declared. There are two 
translation rules to remember

* Remove any leading dashes e.g., `-` or `--`, from the argument name
* Replace any embedded dash `-` within the argument name with an underscore `_`

```python
print(f'host is {args.hostname}')
print(f'project {args.project}')
print(f'label is {args.label}')
print(f'out_dir is {args.output_dir}')
```
