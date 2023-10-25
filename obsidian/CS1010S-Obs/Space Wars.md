# Wishful Thinking
## Objects
- ships
- space stations
- other objects
# Implementation
## Objects
### Ship
```python
class Ship:
	def __init__(self, p, v, num_torps):
		self.position = p
		self.velocity = v
		self.num_torps = num_torps
	def move(self):
		self.position = ...
	def fire_torps(self):
		if num_torps > 0:
			self.num_torps -= 1
		else:
			return "No torpedoes!"
```
So...
```python
enterprise = Ship((10,10), (5,0), 3)
falcon = Ship((-10,10), (10,0), 8)
print(enterprise) # => <__main__.Ship object at 0xaljsdhf>
```
### Torpedo
```python
class Torpedo:
	def __init__(self, p, v):
		self.position = p
		self.velocity = v
	def move(self):
		self.position = ...
	def explode(self):
		print("torpedo goes off!")
```
Now we see some similarities... such as the properties `position`, `velocity`, and the method `move`. We can conduct a [[Functional Abstraction]]. In the context of [[Object-Oriented Programming (OOP)]], we call this [[Inheritance]].
# [[Inheritance]]
