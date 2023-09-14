Similar to [[Functional Abstraction]], we can abstract [[Function|functions]].
- Abstract away irrelevant details
- Expose what is necessary
- Separate usage from implementation
- Capture common programming patterns
- Serves as a building block for other compound data
# Guidelines for Compound Data
1. [[Constructors]]
2. [[Selector]]
3. [[Predicates]]
4. [[Printers]]
# Wishful Thinking
> Wouldn't it be nice to have
> - a function that can create a rational number
> - access the denominator and numerator of that number

Ok, now we implement these functions!
The data structure that can help us is a [[Tuples|tuple]].