Exploit commonality to share structure and behaviour.
- [[Class|Classes]] that exhibit similar functionality should *inherit* from the same base class, called the **superclass**.
- A class that inherits from another is called the **subclass**.
- **Subclass** specialises the **superclass**.
# Example: [[Space Wars]]
# Implementation
```python
class A:
	def __init__(self, var):
		self.var = var
	def foo(self):
		print(self.var)

class B(A): # B is a subclass of A, it inherits properties.
	def bar(self):
		print("this is B")
```

In general, for some superclass `Superclass` and subclass `Subclass`:
```python
class Subclass(Superclass):
	...
```
# Relationships
Two kinds of relationships between A and B:
- A *is-a* B (B is a subclass of A)
- A *has-a* B (A contains B as a property)
# `super()` method: Going up one level
```python
class NamedObject(object):
	def __init__(self, name):
		self.name = name.lower() # name.lower() cascades down
		
class MobileObject(NamedObject):
	def __init__(self, new, location):
		# self.name = name <--- usually done this way
		super().__init__(name) # looks to the superclass NamedObject
		self.location = location
```