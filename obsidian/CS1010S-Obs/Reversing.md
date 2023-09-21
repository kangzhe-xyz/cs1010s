# Recursive Method
The following is a [[Recursive Process|recursive]] method.
```python
def reverse(seq):
	if seq == ():
		return ()
	else:
		return reverse(seq[1:]) + (seq[0],) # Bring the first element to the back. It needs to be a tuple for concatenation.
```
This is just a fancy way of implementing `seq[::-1]`.
## [[Order of Growth]]
[[Time Complexity]]: $\mathcal O(n^2)$
[[Space Complexity]]: $\mathcal O(n^2)$
# Iterative Method
