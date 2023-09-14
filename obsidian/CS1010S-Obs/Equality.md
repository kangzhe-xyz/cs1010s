We can define equality in two ways:
 ![[Identity]]
 ![[Equivalence]]
Identity is not equivalence!
# Example
```python
x = (1, 2)
y = (1, 2)
z = x

x is y # => False. They just have the same value.
z is x # => True. Pointing to the same object.
x == y # => True

100 ** 100 is 100 ** 100 # => False. They are stored in different memory addresses
```

```python
('a', 'b') is ('a', 'b') # => True

x = ('a', 'b') 
y = ('a', 'b')
x is y # => False
```

# Conclusion
Avoid the `is` operator, especially when you meant `==`.
