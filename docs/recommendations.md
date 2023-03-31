# Recommendations

Here's a brief list of recommended Python packages.

## pipenv
There is no universally accepted toolchain for building Python applications in a simple 
(nevermind [deterministic](https://en.wikipedia.org/wiki/Reproducible_builds)) way. 
I've tried a few different offerings, but ultimately landed on 
[pipenv](https://github.com/pypa/pipenv). There's also
[poetry](https://python-poetry.org). Also, supposedly even
[pip](https://pip.pypa.io/en/stable/topics/dependency-resolution/)
now has a dependency resolver! Good times.

## requests
If you need to make HTTP requests, you should check out 
[requests](https://github.com/psf/requests). 
This is perhaps one of the best API designs in the Python ecosystem.

## vcrpy
If you ever need to mock out HTTP responses for testing, I've tried a bunch and landed on  
[vcrpy](https://vcrpy.readthedocs.io/en/latest/).

## flask
Need a web application by the end of the day? Try 
[flask](https://flask.palletsprojects.com/en/1.1.x/).

## mkdocs
Writing documentation? Already know or want to learn Markdown? Try 
[mkdocs](https://github.com/mkdocs/mkdocs/).
