# Virtual environments

_Virtual environments_ will allow you to install and try out as many different 
Python packages as possible. 

## Creating a virtual environment

To create a virtual environment, execute the following _shell_ command

```bash
% python -m venv test
```

This will create a directory named `test`.

## Activating your virtual environment

To activate your virtual environment, execute the following _shell_ command

```bash
% source test/bin/activate
```

You're now using an isolated/sandboxed Python installation under the `test` 
directory. 

!!! note ""
    You should notice that `which python` now points to the Python executable 
    that resided within your virtual environment.

### deactivate

To deactivate the virtual environment, execute the `deactivate` _shell_ command

```bash
(test) % deactivate
```

!!! note ""
    You should notice that `which python` now points to the system installed 
    Python executable. 

## `pip`

The main package installer for Python is
[`pip`](https://pip.pypa.io/en/stable/).

### upgrade pip

For the rest of this tutorial, you should only run `pip` from within an 
_activated virtual environment_. Before you proceed any further, you should 
upgrade `pip`

```bash
(test) % pip install --upgrade pip
```

Now you can install external packages such as `pydicom`

```bash
(test) % pip install pydicom
```

### dependency management

You may notice that when you install an external package such as `pydicom`, 
this triggers the installation of additional packages. This creates a 
_dependency graph_. If we were to explore the dependency graph for the 
[`yaxil`](https://github.com/harvard-nrg/yaxil)
library, you would see the following

!!! note ""
    The following graph was rendered with
    [`pipenv`](https://pipenv.pypa.io/en/latest/)

```text
yaxil==0.4.3
  - arrow [required: Any, installed: 0.15.5]
    - python-dateutil [required: Any, installed: 2.8.1]
      - six [required: >=1.5, installed: 1.14.0]
  - lxml [required: Any, installed: 4.5.0]
  - pyaml [required: Any, installed: 19.12.0]
    - PyYAML [required: Any, installed: 5.3]
  - pydicom [required: Any, installed: 1.4.1]
  - requests [required: Any, installed: 2.22.0]
    - certifi [required: >=2017.4.17, installed: 2019.11.28]
    - chardet [required: >=3.0.2,<3.1.0, installed: 3.0.4]
    - idna [required: >=2.5,<2.9, installed: 2.8]
    - urllib3 [required: >=1.21.1,<1.26,!=1.25.1,!=1.25.0, installed: 1.25.8]
  - six [required: Any, installed: 1.14.0]
```

You can see that `yaxil` depends on `arrow`, `lxml`, `pydicom`, `requests`, 
and `six` and in turn, each of those dependencies have their own dependencies.

Diving deeper, you'll see that `arrow` depends on `python-dateutil` which 
in turn depends on `six >= 1.5`. Coincidentally, `yaxil` also depends on `six` 
and will accept `Any` version. But what if it didn't? If these two packages 
had conflicting requirements, there would be a _dependency conflict_.

