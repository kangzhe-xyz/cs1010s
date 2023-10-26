# Motivation
## Functional Overloading
Functions that have the same name but different interfaces.
### Example
```python 
def add(x):
	return x + 2

def add(x, y)
	return x + y + 2

add(3, 4) # => 9
add(2) # => Error!
```
## Functional Overriding
If sometimes you have multiple functions but named the same way, depending on how it is defined it might override another definition.
For example, see this usage of [[Inheritance]]
```python
class A(object):
	def print(self):
		print("In class A")
class B(A):
	def print(self):
		print("In class B")
		super().print()
class C(A):
	pass
```
Then
```bash
>>> a_obj = A()
>>> b_obj = B()
>>> c_obj = C()

>>> a_obj.print()
In class A

>>> b_obj.print()
In class B # this one from its own defintion
In class A # this one from super().print()

>>> c_obj.print()
In class A # no method print() in C, so it looks in A
```

