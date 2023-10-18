A mapping from key to value.
$$\mathtt{dict} \colon \mathtt{key} \to \mathtt{value}.$$
```python
lecturers = {
	# key    : value
	'dcsaysp': 'Adi',
	'dcsashi': 'Ashish',
	'dcsdlsw': 'Daren'
}
```

We call each line a key-value pair.
Think of it as a lookup table

| Key     | Value  |
| ------- | ------ |
| dcsaysp | Adi    |
| dcsashi | Ashish |
| dcsdlsw | Daren  |

# Link to [[Sorts]]
```python
sorted(seq, key=...)
```
# Retrieval
Retrieve values using the key.
```python
lecturers['dcsaysp'] # => 'Adi'
```
# Comparison between [[Dictionary]] and [[Lists]]
## Vending Machines
In vending machine, you type a number, the thing gives you the item.
This is a list/tuple.
```python
vm = ['M&M', 'Twix', 'Milky Way', 'Oreo']
vm[1] # => 'Twix'
```
## Japan
You are not inputting a number
```python
vmj = {
	   'Beef Noodle Big': '🍜',
	   'Beef Noodle Small': '🍲'
}
vmj['Beef Noodle Big'] # => '🍜'
```
# Usefulness
## Example: Keeping track of stock
```python
my_stock = {
			'🍎': 450,
			'🍊': 412
}
my_stock['🍎'] # => 450
my_stock['🍎'] + my_stock['🍊'] # => 862
```
# Methods

| code               | operation | time            |
| ------------------ | --------- | --------------- |
| `my_stock['🍎']`   | access    | $\mathcal O(1)$ |
| `my_stock['🍎'] = 200`   | update    | $\mathcal O(1)$ |
| `del my_stock['🍎']` | delete    | $\mathcal O(1)$ |
## Accessing
```python
my_stock['🍐'] # => KeyError: '🍐'
my_stock.get('🍐', 0) # this is a try-except, if 🍐 failst then return 0. By default this would be None.
my_stock.get('🍐', None) # equivalent to line 1
```
## Updating
```python
my_stock['🍐'] = 200
my_stock # => {'🍎': 450, '🍊': 412, '🍐': 200} # if key DNE, create
my_stock['🍊'] = 200
my_stock # => {'🍎': 450, '🍊': 200, '🍐': 200} # if key exist, update
```
## Removal?
One can erase the values, but **not** the key.
```python
my_stock['🍐'] = 200
my_stock # => {'🍎': 450, '🍊': 412, '🍐': 200} # if key DNE, create
my_stock['🍊'] = 200
my_stock # => {'🍎': 450, '🍊': 200, '🍐': 200} # if key exist, update
```
### Pop and Delete
```python
my_stock.pop('🍐')
my_stock # => {'🍎': 450, '🍊': None}

del my_stock['🍊']
my_stock # => {'🍎': 450}
```
## Other Methods
| Method         | Operation                                               |
| -------------- | ------------------------------------------------------- |
| `dct.clear()`  | clear the elements in `dct`                             |
| `dct.copy()`   | returns shallow copy of `dct`                           |
| `dct.keys()`   | returns sequence of keys in `dct`                       |
| `dct.values()` | returns a sequence of values in `dct`                   |
| `dct.items()`  | returns a sequence of all `(key, value)` pairs in `dct` |
# Example Implementation
## Example 1: Anagram
> Two strings are anagrams of one another if they can be formed from each other by rearranging the letters using all the original letters.

Using dictionaries, count the number of occurrences in each character.
```python
def counting(s):
	res = {}
	for char in s:
		res[char] = res.get(char,0) + 1
	return res
```
## Example 2: DNA to RNA
> Transcription of DNA to RNA is given by
> - T to A
> - A to U
> - C to G
> - G to C

Example: "ATCG" will map to "UAGC".

```python
def transcribe(dna):
	mapping = {
		"A": "U",
		"T": "A",
		"C": "G",
		"G": "C"
	}
	rna = ""
	for base in dna:
		rna += mapping[base]
	return rna
```
