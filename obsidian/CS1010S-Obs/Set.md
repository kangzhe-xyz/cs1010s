A set is an [[Unordered Representations]] of elements without duplicates.
# Idempotence
```python
my_lst = [1, 2, 3, 2, 1]
print(my_lst) # => [1, 2, 3, 2, 1]
print(my_lst[3]) # => 2

my_set = {1, 2, 3, 2, 1}
print(my_set) # => {1, 2, 3}
print(my_set[2]) # TypeError. No indexing in sets.
```
# Declaration
To declare the empty set,
```python
my_set = set()
```
> **Warning:** Note that `{}` will define an empty [[Dictionary]].
```python
my_set = set()
type(my_set) # => <class 'set'>

my_new_set = {}
type(my_new_set) # => <class 'dict'>
```
# Unordering
```python
{1, 2, 3} == {3, 2, 1} # => True
(1, 2, 3) == (3, 2, 1) # => False
```
A [[Lists|list]] **cannot** be a member of a set.
```python
{1, [2]} # => Error
```
A [[Set]] also cannot be a member of a set.
In general, if the item is [[Mutation|mutable]] 
# Set Operations
Union, Intersection, Difference.
Analogous to $A \cap B$, $A \cup B$, $A \setminus B$.