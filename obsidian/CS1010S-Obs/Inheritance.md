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
# Multiple Class Inheritance
## Example: [[Speakers]]
```python
class SingingCoolLecturer(CoolLecturer, Singer):
	def __init__(self, fav_phrase):
		super().__init__(fav_phrase) # 1. which is the super?
		super().sing() # 2. which one?

```
1. In python, the default `super` is going to be from left-to-right.
	1. Checks `CoolLecturer` first.
	2. Since `CoolLecturer` has `__init__` method, it will use that.
2. In python, the default `super` is going to be from left-to-right.
	1. Checks `CoolLecturer` first.
	2. No `sing()` in `CoolLecturer`. 
	3. Go up.
	4. No `sing()` in the super of `CoolLecturer`. Go up again.
	5. Until terminate, no `sing()` at all.
	6. Now try `Singer`.
	7. Repeat.
## Algorithm for Inheritance in Python
1. Traverse up the leftmost branch. 
2. If the entire branch does not exist, then we go to the previous junction and traverse up the next (right to first) branch.
3. Repeat until the method or attribute is found.
## More example
Suppose `Singer` inherits `Speaker`.
```python
class Singer(Speaker)
	def say(self, stuff):
		super().say("tra-la-la -- " + stuff)
	def sing(self):
		print("tra-la-la")
```
So how would  
```python
class SingingCoolLecturer(CoolLecturer, Singer):
	def __init__(self, fav_phrase):
		super().__init__(fav_phrase) # 1. which is the super?
		super().sing() # 2. which one?
```
be resolved now?
Use the algorithm.
1. Traverse up the left one, `CoolLecturer`.
2. If not found, go up `CoolLecturer` to `Lecturer`.
	1. Found? No.
	2. Does `Lecturer` share any child classes? No.
3. Go up `CoolLecturer` to `Speaker`.
	1. Found? No.
	2. Does `Speaker` share any child classes? Yes! `Singer`.
	3. Is `Singer` inherited by `SingingCoolLecturer`? Yes!
4. Go to `Singer` branch.
	1. Found? Yes.
5. So we use the `Singer` definition for `sing()`. We are done.
6. Since this whole branch not found, 