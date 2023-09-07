# Example
## Naive step counter
Consider the iterative factorial function!
```python
def fact(n):
	res, counter = 1, 1
	steps = 2 # 2 assignments
	while counter <= n:
		res = res * counter
		counter = counter + 1
		steps = steps + 5 # 5 steps every loop
	print(steps)
	return res
```
We observe that the growth in time complexity is kind of linear as we increase `n`. 
We denote this with the [[Big-O Notation]]. More about this later.
## Can we be more precise?
- How much time does each operation take, exactly?
- Are they all taking the same time?
### Time Table of Operations
| Operations | Time needed / ms |
| ---------- | ---------------- |
| Assignment | a                |
| Arithmetic | b                |
| Relational | c                |
We see that after some calculations,
Let $T(n)$ denote the time needed for `fact` with respect other input $n$.
$$T(n) = 2a + n(c + 1 + 2a + 2b).$$
This is quite an ugly operation. We can rewrite this as a kind of polynomial. It is equivalent to
$$T(n) = A' + nB'$$
and this is a linear equation.
## What about Recursion?
```python
def fact_rec(n):
	if n == 1:
		return 1
	else:
		return n * fact(n-1)
```
There are more calls in this.
```pseudocode
fact(4)
4 * fact(3)
4 * (3 * fact(2))
4 * (3 * (2 * fact(1))
4 * (3 * (2 * (1)))
```
For this one, we have
$$T(n) = c + 2b + T(n-1) = c' + T(n-1) = 2c' + T(n-2) = \cdots$$
Eventually, this reaches $T(n - (n-1)) = T(1)$. 
So we have 
$$T(n) = (n-1) c' + T(1).$$
But we know $T(1) = c$. So we have $T(n) = A' + nB'$ for some constants $A'$ and $B'$.