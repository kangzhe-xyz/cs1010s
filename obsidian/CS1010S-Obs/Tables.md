Tables are basically 2-dimensional [[Tuples]]. They are usually stored as [[Files]].
How can we represent a table in Python?
Where to get the data? from [[Files]]!
# Comma Separated Value files (CSV)
```python
def read_csv(csvfilename):
	rows = ()
	with open(csvfilename, 'r') as csvfile:
		file_reader = csv.reader(csvfile)
		for row in file_reader:
			rows += (tuple(row),)
		return rows
```
We can use [[HOF Sequences#HOF `map`]] and [[HOF Sequences#HOF `filter`]] to help us do [[Data Wrangling]].