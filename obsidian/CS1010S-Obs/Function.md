# Summary
Enter some input $x$. Get some output $f(x)$.
Don't care how it works. Just know what it does.
# Definition (Mathematical)
A function $f \colon A \to B$ is the set of ordered pairs $(a,b)$ where $a \in A$ and $b \in B$ such that all elements of $A$ are part of an ordered pair, and each element of $a$ exist in exactly one of the ordered pair.
# Implementation
```python
def function(parameters):
	# body
	return result
```

| Keyword      | Explanation                                        |
| ------------ | -------------------------------------------------- |
| `def`        | `def` keyword. To define a function.               |
| `function`   | The name of the function. Follow PEP8 guidelines.  |
| `parameters` | Inputs to the function. Can take multiple.         |
| `return`     | `return` keyword. The final value of the function. |
| `result`     | What to be returned.                                                   |
# Example
## Squaring a number
A function to square a number.
```python
def sqr(x):
	return x * x # return statement

sqr(5) # => 25
```
## Finding the magnitude
A function to find the magnitude of a vector $\begin{pmatrix}a \\ b\end{pmatrix}$.
```python
def magintude(a,b):
	return (sqr(a) + sqr(b)) ** 0.5 # return statement, reuse of the sqr(r) function.
```
