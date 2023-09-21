# What it is
A sequence is sequential data, *represented* by [[Tuples]].
It *may not necessarily be a tuple*.
# Implementation
To get the first element:
```python
seq[0] # may not be a tuple
```
To get the rest of elements (basically, index `1` and onwards):
```python
seq[1:] # always a tuple, this is slicing
```
To get the `n`th element:
```python
seq[n] # may not be a tuple
```
## Example
If a sequence is a tuple containing a single integer 4,
```python
seq = (4,) # the comma is important! this is a singleton tuple.
seq[0]     # => 4
seq[1:]    # => ()
```
# Examples
- [[Reversing|Reversing a Sequence]]
- [[Scaling a Sequence]]
- [[HOF Sequences]]
- [[Iterables]]