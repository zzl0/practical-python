
# 3.1 Scripting

> Also, a little known fact is that Python runs a bit faster if you use functions.

https://stackoverflow.com/questions/11241523/why-does-python-code-run-faster-in-a-function

The short answer is that it is faster to store local variables than globals.

# 3.6 Design Discussion

In this section we reconsider a design decision made earlier.

### Filenames versus Iterables

Compare these two programs that return the same output.

```python
# Provide a filename
def read_data(filename):
    records = []
    with open(filename) as f:
        for line in f:
            ...
            records.append(r)
    return records

d = read_data('file.csv')
```

```python
# Provide lines
def read_data(lines):
    records = []
    for line in lines:
        ...
        records.append(r)
    return records

with open('file.csv') as f:
    d = read_data(f)
```

* Which of these functions do you prefer? Why?
* Which of these functions is more flexible?

### Deep Idea: "Duck Typing"

[Duck Typing](https://en.wikipedia.org/wiki/Duck_typing) is a computer
programming concept to determine whether an object can be used for a
particular purpose.  It is an application of the [duck
test](https://en.wikipedia.org/wiki/Duck_test).

> If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.

In the second version of `read_data()` above, the function expects any
iterable object. Not just the lines of a file.

```python
def read_data(lines):
    records = []
    for line in lines:
        ...
        records.append(r)
    return records
```

This means that we can use it with other *lines*.

```python
# A CSV file
lines = open('data.csv')
data = read_data(lines)

# A zipped file
lines = gzip.open('data.csv.gz','rt')
data = read_data(lines)

# The Standard Input
lines = sys.stdin
data = read_data(lines)

# A list of strings
lines = ['ACME,50,91.1','IBM,75,123.45', ... ]
data = read_data(lines)
```

There is considerable flexibility with this design.

*Question: Should we embrace or fight this flexibility?*

### Library Design Best Practices

Code libraries are often better served by embracing flexibility.
Don't restrict your options.  With great flexibility comes great power.

# 5.1 Dictionaries Revisited

### The "Mixin" Pattern

The *Mixin* pattern is a class with a fragment of code.

```python
class Loud:
    def noise(self):
        return super().noise().upper()
```

This class is not usable in isolation.
It mixes with other classes via inheritance.

```python
class LoudDog(Loud, Dog):
    pass

class LoudBike(Loud, Bike):
    pass
```

Miraculously, loudness was now implemented just once and reused
in two completely unrelated classes.  This sort of trick is one
of the primary uses of multiple inheritance in Python.

### Why `super()`

Always use `super()` when overriding methods.

```python
class Loud:
    def noise(self):
        return super().noise().upper()
```

`super()` delegates to the *next class* on the MRO.

The tricky bit is that you don't know what it is.  You especially don't
know what it is if multiple inheritance is being used.

### Some Cautions

Multiple inheritance is a powerful tool. Remember that with power
comes responsibility.  Frameworks / libraries sometimes use it for
advanced features involving composition of components.  Now, forget
that you saw that.


# 6.1 Interation Protocol

One important observation about this--generally code is considered
"Pythonic" if it speaks the common vocabulary of how other parts of
Python normally work.  For container objects, supporting iteration,
indexing, containment, and other kinds of operators is an important
part of this.


# 6.4 More Generators

### Why Generators

* Many problems are much more clearly expressed in terms of iteration.
  * Looping over a collection of items and performing some kind of operation (searching, replacing, modifying, etc.).
  * Processing pipelines can be applied to a wide range of data processing problems.
* Better memory efficiency.
  * Only produce values when needed.
  * Contrast to constructing giant lists.
  * Can operate on streaming data
* Generators encourage code reuse
  * Separates the *iteration* from code that uses the iteration
  * You can build a toolbox of interesting iteration functions and *mix-n-match*.
