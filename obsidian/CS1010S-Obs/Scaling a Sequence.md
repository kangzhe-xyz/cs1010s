We want to scale all elements of a sequence by some number.
```python
>>> scale_seq((1, 2, 3, 4), 4)
(3, 6, 9, 12)
```
# Recursive Process
Implementation by [[Recursive Process]]
```python
def scale_seq(seq, factor):
	if seq == ():
		return ()
	else:
		return (seq[0] * factor) + scale_seq(seq[1:], factor)
```
This code looks similar to [[Reversing#Recursive Method]].
## [[Order of Growth]]
[[Time Complexity]]:
[[Space Complexity]]:
# Iterative Process
Implementation by [[Iterative Process]]
```python
def scale_seq(seq, factor):
	res = () # initialise empty
	for elem in seq: # loop across all
		res = res + (elem * factor,) # calculate element-wise 
	return res # final
```
## [[Order of Growth]]
[[Time Complexity]]: $\mathcal O(n^2)$
[[Space Complexity]]: $\mathcal O(n)$