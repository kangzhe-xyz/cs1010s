# Recall: [[Data Abstraction]]
So far we have worked with certain abstract data types (ADT). However, these data types are just loosely related to certain [[Function|functions]] that conduct some operation on the ADT.
## Example: Bank Account
### [[Constructors]]
```python
def make_acct(name, bal):
	return (name, bal)
```
### [[Mutation]]
```python
def get_name(acct):
	return acct[0]

def get_bal(acct):
	return acct[1]

def set_bal(acct, bal):
	return make_acct(get_name(acct), bal)
```
## The Issues
The operations do not keep the same tuple. It changes the tuple every time. It's not the same account.
Potential solution is to use [[Lists]].
```python
>>> ben_acct = make_acct('ben', 1000)
>>> deposit(ben_acct, 40)
>>> print(ben_acct) # => ('ben', 1000)
```
In the printer, it exposes the structure. Even with list, it will expose the structure.
Now you can break the thing!
```python
>>> deposit((20, 40), 40)
```
Now we have a name!
- Data and functions are not **encapsulated**. 
- The functions are not legally *bound* to the ADT. They are not a "contract".
- The function has to be uniquely named. If we want to abstract this abstraction, it'll be quite limited.
# Solution: OOP
1. [[Data Abstraction]]: express intent over implementation
2. [[Encapsulation]]: binding data with their functions
3. [[Polymorphism]]: same interface, but different implementation
4. [[Inheritance]]: ability to extend the existing functionality.
# Implementation
We can define a [[Class]] for the `BankAccount` which is an object.
```python
class BankAccount(object):
	def __init__(self, name, bal):
		self.name = name
		self.bal = bal
		
	def deposit(self, amt):
		self.bal += amt
		
	def withdraw(self, amt):
		if self.bal < amt:
			return "Insufficient Balance"
		else:
			self.bal -= amt
			return self.bal
```
An instance of the class is called an [[Object]].
We initialise an **object** through the class now, instead of `make_account`.
```python
ben_acct = BankAccount('ben', 1000)
ben_acct.deposit(40)
ben_acct.withdraw(40)
```