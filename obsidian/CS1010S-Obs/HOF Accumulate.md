#HOF 
Defined in [[CS1010S-Lec-06+Working+with+Sequence.pdf]]
```python
accumulate(fn: any, init: any, seq: any) -> any
```
# Implementation

```python
def accumulate(fn, init, seq):
	if seq == ():
		return init
	else:
		return fn(seq[0], accumulate(fn, init, seq[1:]))
```