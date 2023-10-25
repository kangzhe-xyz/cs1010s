#HOF
Defined in [[CS1010S-Lec-04 Order of Growth and Higher-Order Functions.pdf]]
# Implementation
```python
def fold(op, f, n):
	if n == 0:
		return f(0)
	else:
		return op(fold(op, f, n-1), f(n))
```
# Example
```python
tup = (1, 2, 3)
fold(
	 lambda x, y: x + y,
	 lambda x: x,
	 5
)
```