A type of [[Sequences]] that can be [[Mutation|mutated]]. [[Tuples]] by comparison are not mutable.
# When to use which
| Data Type       | Tuple | List |
| --------------- | ----- | ---- |
| Need to mutate? | No    | Yes  |
| Same data type? | No    | Yes  |

# Operations
| Code       | Operation                               |
| ---------- | --------------------------------------- |
| `len(seq)` | returns the number of elements in `seq` |
| `max(seq)` | returns the "largest" element in `seq`  |
| `min(seq)` | returns the minimum value on `seq`      |
## [[Mutation]] 
| Code                    | Operation                                                                   | What exactly? |
| ----------------------- | --------------------------------------------------------------------------- | ------------- |
| `lst.append(elem)`      | modifies `lst` by adding element `elem` at the end of the list `lst`        | modificaiton  |
| `lst.extend(seq)`       | modifies `lst` by addign each element of `seq` at the end of the list `lst` | modification  |
| `lst.copy()`            | returns a "shallow copy" of `lst`                                           | modification  |
| `lst.reverse()`         | modifies `lst` by reversing it                                              | modification  |
| `lst.insert(idx, elem)` | modifies `lst` by inserting element `elem` to index `idx` of the list `lst` | modification  |
| `lst.pop()`             |                                                                             |               |

```python
l1 = [1, 2]
lst = [l1.copy(), 2, 3, l1.copy()]
print(lst) # => 
lst.remove(l1) # removal by equivalence
print(lst) # => 
```
### Recursive definition of self
```python
lst = [1, 2, 3]
print(lst) # => [1, 2, 3]
lst[2] = lst
print(lst) # => [1, 2, [...]]
```