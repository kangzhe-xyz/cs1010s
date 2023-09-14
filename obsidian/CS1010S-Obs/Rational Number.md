#Example 
# Definition
A rational number $r$ can be expressed in the form $\frac{p}{q}$ such that $p, q \in \mathbb{Z}$ and $q \neq 0$.
# [[Data Abstraction]]
> `float` is imprecise. It is better to work with fractions.

We want to work with fractions: such that $\frac{1}{10} + \frac{2}{10} = \frac{3}{10}$. Precise!
### Addition
$$\frac{n_1}{d_1} + \frac{n_2}{d_2} = \frac{n_1 d_2 + n_2 d_1}{d_1 d_2}.$$
Let's abstract $n_x$ as `numer(x)` and $d_x$ as `denom(x)`.
Then we can define
```python
def add_rat(x, y):
	n1, d1 = numer(x), denom(x)
	n2, d2 = numer(y), denom(y)
	return make_rat(n_1 * d_2 + n_2 * d_1, d_1 * d_2)
```
# Wishful Thinking
Wouldn't it be nice if we have 
- `make_rat(n, d)`
- `numer(rat_number)`
- `denom(rat_number)`
# Define them!
```python
def make_rat(n: int, d: int) -> (int, int):
	return (n, d)

def numer(rat: (int, int)) -> int:
	return(rat[0])

def denom(rat: (int, int)) -> int:
	return(rat[1])
```