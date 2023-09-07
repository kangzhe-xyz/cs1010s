# Recap
![[Function#Summary]]
# Abstraction
Consider the code that sums the integers from $a$ to $b$.
```python
def sum_int(a,b):
	if a > b:
		return 0
	else:
		return a + sum_int(a+1, b)
```
Consider the code that sums the squares of integers from $a$ to $b$.
```python
def sum_sqr(a,b):
	if a > b:
		return 0
	else:
		return sqr(a) + sum_sqr(a+1, b)
```
So we see there are commonalities. We generalise these.
```python
def <name>(a,b):
	if a > b:
		return 0
	else:
		return <f1>(a) + <name>(<f2>(a), b)
```
See that functions can be arguments!
We get
```python
def sum(term, a, next, b)
	if a > b:
		return 0
	else:
		return term(a) + sum(term, next(a), next, b)
```
So we need to define `term` and `next`.
## Mapping
| name | variable   |
| ---- | --- |
| term | f   |
| a    | x   |
| next | g   |
| b    | y    |
So if we wanted to call `sum_sqr`, we can write
```python
def sum_sqr(a,b):
	return sum(
		sqr,
		a,
		lambda x: x+1,
		b	
	)
```