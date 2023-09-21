#Example
The Fibonacci sequence $\{F_n\}_{n \in \mathbb{N}}$ is defined by
$$F_0 = 0, \quad F_1 = 1, \quad F_{n+2} = F_{n+1} + F_n.$$
# [[Recursive Process]]
We look at the [[Recursion|recursive approach]].
```python
def fib(n):
	if n <= 1:
		return 0
	else:
		return fib(n-1) + fib(n-2)
```
The [[Time Complexity]] of this guy is $O(2^n)$. Draw the recursion tree to verify this.
The [[Space Complexity]] is $O(n)$. Space can be reused. At any one time we are only looking at one branch of the tree, and that space of the tree, once computed, can be reused by a neighbour branch.
# Thinking with [[Sequences]]
We use the [[HOF Sequences]] ideas.
## Problem Statement
> Find the list of even `fib(k)` for all `k` greater than $0$ up to a given integer $n$.

## Implementation
