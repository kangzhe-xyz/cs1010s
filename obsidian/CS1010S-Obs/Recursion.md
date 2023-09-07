A recursive function is a [[Function]] that calls itself.
# Example
Suppose we want to find out which row number we are in.
## Strategy 1: [[Iterative Process]]
1. Stand up, go to row 1, start counting for 1.
2. Add 1 when you go backwards.
3. When you reach your row, that number you end up with is your answer.
## Strategy 2: [[Recursive Process]]
1. Ask the person in front of you. This is called a [[Deferred Operation]].
2. The person in front uses the same strategy. This is the [[Recursive Step]].
3. This continues until the person in front replies "row 1". This is the [[Base Case]].
In recursion, the problem is split up into many subproblems. 
It keeps going on until it reaches the base case.
Then we work backwards.
# Example: ![[Factorial]]
## Factorial: Iteration
```python
def factorial(n):
	product = 1
	while n > 1:
		product = product * n
		n = n - 1
	return product
```
## Factorial: Recursion
```python
def factorial(n):
	if n <= 1:
		return 1
	else:
		return n * factorial(n-1)
```
We call this a [[Linear Recursion]]. The function `factorial(n)` is called again at most once.
# Example: ![[Euler's Constant]]
## Euler's Constant: Recursion
```python
def find_e(n):
	if n == 0:
		return 1
	else:
		return 1/fact(n) + find_e(n-1)
```

| Component             | Expression      |
| --------------------- | --------------- |
| Initial value         | `1`             |
| Terminating Condition | `n == 0`        |
| Deferred Operation    | `1 / fact(n) +` |
| Next Argument         | `n-1`           |
## Euler's Constant: Iteration
```python
def find_e(n):
	res = 1
	while not (n == 0):
		res = 1/fact(n) + res
```
# Example: `my_sum`
Write a program to find 
$$ 1 \times 2 + 2 \times 3 + \cdots + n \times (n+1). $$
```python
def my_sum(n):
	res = 0
	for i in range(1,n+1):
		res += i * i+1
	return res
```
# Example: Primality Testing
```python
def is_prime(n):
	for i in range(2,n):
		if is_divide(i,n):
			result = False
		else:
			result = True
		return result
```