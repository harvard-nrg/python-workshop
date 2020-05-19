# Installing packages

!!! attention "Read this section to the end before doing anything"
    I encourage you to read this entire section before attempting to install 
    anything.

Python has a thriving ecosystem and you should absolutely install and try as m
any different libraries as possible. The following section will walk you 
through most of the installation options at your disposal.

## A brief history

The original package manager for Python was `easy_install`, but you 
shouldn't use it to install anything except for
[`pip`](https://pip.pypa.io/en/stable/)

```bash
sudo easy_install pip
```

## `pip install`

The most basic command `pip` offers to install packages is

!!! attention ""
    This command is for illustrative purposes. Don't run it.

```bash
pip install pydicom
```

Unfortunatley, `pip` will by default attempt to install the package into a 
system location which requires 
[administrative](https://en.wikipedia.org/wiki/Superuser)
privileges. More often than not, you're not going to be able to use this 
option.

## `pip install --user`

You _can_ however instruct `pip` to install packages into your home directory 
using

```python
pip install --user pydicom
```

This will install the package under `~/.local` on Linux or `~/Library/Python` 
on macOS. To install into a custom location, there is also the `--target` 
option. 

!!! note "Dependency conflicts"
    You may run into issues when working on two or more projects that depend 
    on different versions of the same package. This is an important use case 
    for virtual environments. Keep reading. 

## Virtual environments

Ideally, for each software project you would have a separate Python 
installation and within that installation you could control exactly which 
external packages are installed. This is the purpose behind 
_virtual environments_. 

!!! attention "virtualenv"
    Prior to Python 3.3, virtual environments were  made possible by way of an 
    external package
    [`virtualenv`](https://virtualenv.pypa.io/en/latest/).
    Fortunately, this functionality is now 
    [<u>built into Python 3</u>](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments)
    without the need for additional installs.

### create

To create a virtual environment, execute the following _shell_ command

```bash
% python -m venv test
```

This will create a directory named `test`. Congratulations 🎉 you now have a 
virtual environment.

!!! question "Where is Python installed"
    Before moving forward, take note of the location of the `python` executable 
    on your system. This location will change after you've activated your 
    virtual environment

    ```bash
    which python
    ```

### activate

To activate your virtual environment, source the `activation` script

```bash
% source test/bin/activate
```

You shoule notice the string `(test)` has been prepended to your shell prompt.
You're now using an isolated Python installation living under the `test` 
directory. You may also notice that `which python` now points to the `python` 
executable under your virtual environment.

### deactivate

To deactivate the virtual environment, execute the `deactivate` command. 
Deactivation will return you to the original Python installation 

```bash
(test) % deactivate
```

### installing packages

Once your virtual environment has been activated, you can proceed to install 
any external packages. These will be conveniently installed under your virtual 
environment directory

```bash
(test) % pip install pydicom
```

## Dependency management

The deeper you dive into dependency management, the more you're going to find. 
Reading up on
[deterministic builds](https://en.wikipedia.org/wiki/Reproducible_builds)
is a fun place to start.

### dependency graph

Just as you have your dependencies, you must also consider that your 
dependencies have their own dependencies too. You might even have overlapping 
dependencies. This is where things can get messy.

If we explore the dependency graph for the 
[`yaxil`](https://github.com/harvard-nrg/yaxil)
project — which is a rather small project — you'll see the following 
dependency graph

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

You can see here that `yaxil` depends directly on `arrow`, `lxml`, `pydicom`, 
`requests`, and `six`. That's just at the root level. Each of those 
dependencies have their own dependencies too, sometimes with even greater 
specificity. Looking more closely, you'll see that `arrow` depends on 
`python-dateutil` which in turn depends on `six >= 1.5`. Coincidentally, 
`yaxil` also depends on `six`. Fortunately, it will accept any version. But 
what if it didn't? If these two packages had conflicting requirements, there 
would be a _dependency conflict_ and you may not be alerted to this.

### `pipenv`

[Pipenv](https://pipenv.pypa.io/en/latest/)
is a wonderful new tool that not only allows you to document your dependencies, 
it can also resolve your dependency graph and let you know if and where you've 
introduced a dependency conflict.

