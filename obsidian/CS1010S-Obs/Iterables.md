The functions [[HOF Sequences#HOF `map`]] and [[HOF Sequences#HOF `filter`]] returns iterables.
```python
>>> x = map(lambda y: y * 2, (1, 2, 3))
>>> x
<map object at (some memory addr)>

>>> for i in x:
...     print(x)
# (no output)
```

Iterables are of **one-time use** (unless converted).