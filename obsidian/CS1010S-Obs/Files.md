Files are useful in storing records.
# Working with Files
## File reading
```python
with open('inputfilename.txt', 'r') as file:
	line = file.readline()
```
## Check End of Line
```python
line == ""
```
## File writing
```python
with open('inputfilename.txt', 'w') as file:
	line = file.writeline()
```
# Example
```python
def metric(filename):
	with open(filename, 'r') as file:
		currword = file.readline()
		longest, shortest = currword, currword
		while currword != '':
			if len(currword) < len(shortest):
				shortest = currword
			if len(currword) > len(longest):
				longest = currword
		return (shortest, longest)
```
An example of a file is [[Tables]].