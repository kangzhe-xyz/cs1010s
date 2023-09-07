# Example
## Iterative Factorial
```python
def fact(n):
	res, counter = 1, 1
	while counter <= n:
		res = res * counter
		counter = counter + 1
	return res
```
### Trace Table
| `res` | `counter` |
| --- | ------- |
| 1   | 1       |
| 1   | 2       |
| 2   | 3       |
| 6   | 4       |
| 24  | 5       |
Let $S(n)$ denote the space needed for `fact` with respect to the input `n`.
Then we have 
$$S(n) = 3 \times c, \quad \text{\(c\) is a constant}.$$
but because `n` does not affect the growth itself, we can drop it and $S(n) = 2c$.
## Recursive Factorial
```python
def fact_rec(n):
	if n == 1:
		return 1
	else:
		return n * fact(n - 1)
```

```pseudocode
fact(4)
4 * fact(3)
4 * (3 * fact(2))
4 * (3 * (2 * fact(1))
4 * (3 * (2 * (1)))
```
Let $S(n)$ denote the space needed for `fact` with respect to the input `n`.
Then 
$$S(n) = cn, \quad \text{\(c\) is a constant}.$$
Space complexity can also be denoted in [[Big-O Notation]].