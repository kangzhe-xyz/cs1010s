Realise the similarity of the [[Reversing#Recursive Method]] and [[Scaling a Sequence#Recursive Process]].
We can define [[Higher Order Function]] based on identifying patterns.
# HOF `map`
We can define a higher-order function called `map`.
```python
def map(f, seq):
	if seq == ():
		return ()
	else:
		return (f(seq[0]),) + map(f, seq[1:])
```
The map basically is a mapping from the original tuple `seq` under the mapping `f`. Mathematically, we have
$$f \colon \mathtt{seq} \to \mathtt{type: tuple}$$
# HOF `filter`
```python
def filter(pred, seq):
	if seq == ():
		return ()
	elif pred(seq[0]):
		return (seq[0]) + filter(pred, seq[1:])
	else:
		return filter(pred, seq[1:])
```
This is useful if we have a sequence `seq`, and some predicate $P(x)$, if the element in `seq` is such that $P(\mathtt{seq})$ fails, then we remove it. Otherwise we keep it. The final output is all the elements in `seq` such that $P(\mathtt{seq})$ holds.
# Benefits
1. Modularity
2. Clarity
3. Flexibility