# Prelude
We do not care about arbitrary constants. 
# Definition
Let $n$ denote the size of the problem. Let $R(n)$ denote the resources needed.
Then $R(n)$ has [[Order of Growth]] of $\mathcal O(f(n))$ written
$$R(n) = \mathcal O(f(n)).$$
If there is a positive constant $k$ and $n_0$ such that 
$$R(n) \leq k \times f(n) \quad \forall n \geq n_0.$$
# Example
Suppose a computation takes $3n+5$ steps to complete.
What is the order of growth?
$$3n + 5 = \mathcal O(n).$$
# How to write Big-O:
- Identify dominant terms, ignore smaller terms.
	- Remember that a term is separated by addition. 
	- The terms in $3x^2 + 2x + 4 \log x + 3^x x^3$ are:
		- $3x^2$
		- $2x$
		- $4 \log x$
		- $3^x x^3$
- Ignore additive or multiplicative constants.
## Example
What is the order of growth for $4n^2 - 1000n + 30000$?
1. We ignore the terms lower than $n^2$ because it is the highest.
2. We ignore the coefficient $4$. 
3. So this is $\mathcal O(n^2)$.

What is the order of growth for $\frac{n}{7} + 200n \log n$?
1. Ignore terms smaller than $200n \log n$.
2. Ignore $200$.
3. So this is $\mathcal O(n \log n)$.
# For now...
Count the number of *basic computational steps*.
- Identify the basic computation steps
- Try a few small values of $n$.
- Extrapolate for really large $n$.
- Look for the *worst-case scenario*.
# Exercises
1. $5n^2 + n = \mathcal{O}(n^2)$
2. $\sqrt{n} + n = \mathcal{O}(n)$
3. $3^n n^2 = \mathcal{O}(3^n n^2)$