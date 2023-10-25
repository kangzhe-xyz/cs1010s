# Definition
A multiset/bag is a [[Set]] that allows for **duplicate elements**. The number of times the element appears is called its **multiplicity**. The arrangements of the elements do not matter.
# Example
$\{a, b, b\} = \{b, a, b\}$
The multiplicity of $b$ is 2.
# Contracts
## Union
Let $X = \{a, a, a, b, b\}$ and $Y = \{b, c, c\}$. 
Then the union of $X$ and $Y$ is
$$ X \cup Y = \{a,a,a,b,b,b,c,c\}. $$
## Intersection
Then the intersection of $X$ and $Y$ is 
$$ X \cap Y = \{b\}.$$
# Implementation of the [[Multiple Representations]]
Choose a representation that has collections.
Different choices will give different time/space complexities.
We have lists, either ordered or unordered.
We also have dicitonary.
## Implementation 1: [[Lists]]
### Predicate: Multiplicity
```python
def multiplicity_of(elem, mset):
	count = 0
	for obj in mset:
		if obj == elem:
			count += 1
	return count
```
This gives $\mathcal O(n)$. (Exercise)
### Predicate: Contains
```python
def contains(elem, mset):
	return elem in mset
```
This gives $\mathcal O(n)$.
### Operation: Union
```python
def union_mset(m1, m2):
	res = make_empty_mset()
	res.extend(m1)
	res.extend(m2)
	return res
```
Exploration: look up merge algorithm.
This gives $\mathcal O(n)$.
### Operation: Intersection
```python
def union_mset(m1, m2):
	res = make_empty_mset()
	for elem in m1:
		if not contains(elem, res):
			n = min(multiplicity_of(elem, m1),
					multiplicity_of(elem, m2))
			res.extend(n * [elem])
	return res
```
This gives $\mathcal O(n^2)$.
### Question
> Can we do better with an **ordered list**?

## Implementation 2: [[Dictionary]]
- Empty set represented by empty dictionary
- Multiset represented by a dictionary of objects as keys and multiplicity as values
### Constructor
```python
def make_empty_set():
	return {}
```
### Predicate: Empty Mset
```python
def is_empty_mset(mset):
	return mset == {}
```
### Predicate: Multiplicity
```python
def multiplicity_of(elem, mset):
	return mset.get(elem, 0)
```
$\mathcal O(1)$
### Predicate: Contains
```python
def contains(elem, mset):
	return elem in mset
```
$\mathcal O(1)$
### Operation: Union
```python
def union_set(m1, m2):
	res = make_empty_mset()
	for elem in m1:
		res[elem] = multiplicity_of(elem, m1) + multiplicity_of(elem, m2)
	for elem in m2:
		res[elem] = multiplicity_of(elem, m1) + multiplicity_of(elem, m2)
	return res
```
$\mathcal O(n)$
### Operation: Intersection
```python
def intersection_mset(m1, m2):
	res = make_empty_mset()
	for elem in m1:
		n = min(multiplicity_of(elem, m1), multiplicity_of(elem, m2))
	if n > 0:
		res[elem] = n
	return res
```