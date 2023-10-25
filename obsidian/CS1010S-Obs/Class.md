A class is a **blueprint** of the [[Data Abstraction|Abstract Data Type]].
# The `__init__` Method: Initialisation
- Special [[Method|method]] to **construct** the object. It is the default [[Constructors|constructor]] of an object.
- It is implicitly called when the object is instantiated.
```python
ben_acct = BankAccount('ben', 1000) 
```
The `__init__` method is run.
# `self`
- Calling the [[Object]] is passed as the first argument.
```python
bill_acct = BankAccount('bill', 200)
bill_acct.deposit(30)
bill_acct.withdraw(20)
```
- `self` refers to the calling object. The instance of the [[Class]].
Accessing the method:
- For some object `obj` and method `mtd`,
```python
obj.mtd(params)
```
# `print()`
The built-in `print()` function calls the `__str__` method of the object.
```python
class BankAccount(object):
	def __init__(self, name, bal):
		self.name = name
		self.bal = bal
		
	def __str__(self):
		return str("Balance is : " + self.bal)
```
# Example: [[Lists]]
Every data type in Python is actually a class.
```python
lst = [1, 2, 3]
lst.append(4)
print(lst)
```
# Example Implementation
1. [[Space Wars]]
2. [[Speakers]]
# `isinstance` vs `type`
```python
class A:
	...

class B(A): # remember, this is B subclass A
	...

isinstance(A(), A) # => True, obvious.
type(A()) == A # => True.

isinstance(B(), A) # => True. Object of type B. Instance of A, due to inheritance.
type(B()) == A # => False
type(B()) == B # => True
```