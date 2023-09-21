# What it is
A data type `tuple` can "bind" data together.
```python
foo = (x, y) # tuple out of x and y

foo[0] # returns 1st component of foo
foo[1] # returns 2nd component of foo
```
First element is index `0`.
## Rule of Thumb
> A tuple must have at least one comma.
> But if you have nothing inside, it is an empty tuple.
# Example
```python
x = (1, 2)
x # => (1, 2)

x[0] # => 1
x[1] # => 2
x[2] # => IndexError. Does not exist.

y = (3, 4)
z = (x, y)

z[0] # => (1, 2)
z[1] # => (3, 4)

z[0][0] # => 1
z[1][1] # => 4
```
We can use [[Box-and-Pointer Notation]].
# More on Tuples
- `()` is the empty tuple.
- `(1,)` is the singleton.
```python
bar = (1, 2)
bat = (3, 4)
foo = bar + bat
foo # => (1, 2, 3, 4,)

foo = (bar, bat)
foo # => ((1,2), (3,4))
```
# Tuple Operations
Similar to ![[String Slicing]] 
## Concatenation
```python
seq = 2 * (2 ,3 ,4)
x = seq[:2] + (0,) + seq[4:]
```
## Copy
```python
x = seq[0:]
```
## Map, Filter
See [[HOF Sequences]]
# Tuple Iterations
See [[Iterative Process]]
```python
x = (4, 2, 1, 3)

count = 0
for i in x:
	print (i)
	count = count + i
print(count) # => 10
```