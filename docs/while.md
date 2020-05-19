# Control of flow

## The `while` loop

The `while` loop will execute the same block of code until a specified 
condition returns `True`. For example

```python
a = 0

while a <= 10:
    print('a is', a)
    a += 1
```

## The infinite loop

A common convention for creating an infinite loop is to use a `while` loop 
given a condition that will never return `False`

!!! danger "Stopping an infinite loop"
    The example below will print `Hello, World!` continuously until 
    you hit <kbd>Control</kbd> + <kbd>C</kbd>

```python
while True:
    print('Hello, World!')
```

