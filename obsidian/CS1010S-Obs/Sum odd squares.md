#Example 
# Problem Statement
Given $n$, add the squares of the odd numbers from $1$ to $n$ inclusive.
Basically, evaluate
$$ \sum_{i = 1}^n i^2. $$
# Implementation
```python
def sum_odd_squares(n):
	res = 0
	for i in range(1, n + 1):      # enumerator
		if i % 2 == 1:             # filter
			res = res + (i * i)    # map
	return res
```
# Alternative View with [[Sequences]]
1. Generate a sequence from $1$ to $n$.
2. Filter the numbers that are not odd.
3. Square the remaining numbers.
4. Return the sum of the numbers in the previous step. 
```python
(5) ---------> (1,2,3,4,5) -----> (1,3,5) --> (1,9,25) ---------> 35
#   enumerate              filter         map          accumulate    
```
## Enumeration
```python
def enumerate_interval(low, high):
	return tuple(range(low, high + 1))
```
## Accumulate
```python
def accumulate(fn, init, seq):
	if seq == ():
		return init
	else:
		return fn(seq[0], accumulate(fn, init, seq[1:]))
```
### Usage
```python
>>> accumulate(lambda x, y: x + y, 0, (1, 2, 3, 4, 5))
15
```
