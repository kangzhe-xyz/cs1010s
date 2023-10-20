# Definition
A matrix is a two-dimensional array of numbers.
# Example
$$ \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix} $$
# Implementation of the [[Multiple Representations]]
## Implementation 1: [[Lists]]
### Constructor: Zero Matrix
Incorrect:
```python
def zero_matrix(row, col):
	res = [[0] * col] * row # aliasing! not correct!
	return res
```
Correct:
```python
def zero_matrix(row, col):
	res = []
	for r in range(row):
		rows = []
		for c in range(col):
			rows.append(0)
		res.append(rows)
	return res
```
### Constructor: Identity Matrix
```python
def identity_matrix(n):
	res = zero_matrix(n) # good practice to reuse
	for i in range(n):
		res[i][i] = 1 # diagonal
	return res
```
### Selector: Get Elements
```python
def get_elem(row, col, matrix):
	return matrix[row][col]
```
## Implementation 2: Dictionary
- Do we need a 2D dictionary? No! One dimension is enough.
- Let the key be `(row, col)`.
- Do we need to store everything? No! 
- We can omit 0. This is a *sparse* matrix.
### Constructor: Zero Matrix
```python
def zero_matrix(row, col):
	res = {}
	return res
```
### Constructor: Identity Matrix
```python
def identity_matrix(n):
	res = zero_matrix(n)
	for i in range(n):
		res[(i, i)] = 1
	return res
```
### Selector: Get Elements
```python
def get_elem(row, col, matrix):
	return matrix[(row, col)]
```