```python
class Speaker(object):
	def say(self, stuff):
		print(stuff)
```
There is no [[Constructors]]. Python calls a *default object constructor*.
```python
p = Speaker()
p.say("Hello World") # => Hello World
p.dance() # => AttributeError: 'Speaker' object has no attribute 'dance'.
```
# Lecturer
A lecturer is a speaker.
Additional method: lecture, and he says the stuff and then adds "You should take notes".
```python
class Lecturer(Speaker):
	def lecture(self, stuff):
		self.say(stuff)
		print("You should take notes")
```
Then
```python
seth = Lecturer()
```
There is no constructor in `Lecturer`, so it checks the superclass `Speaker`. There is none either, so it goes to `Object` and uses the default object constructor.

Tracing: if cannot find in subclass, goes to superclass (parent).
```bash
>>> seth.lecture("Java is easy")
Java is easy
You should take notes
```
and
```bash
>>> seth.say("You have a quiz today")
You have a quiz today
```
and
```bash
>>> seth.dance()
AttributeError
```
# CoolLecturer
- A cool lecturer is a lecturer.
- A cool lecturer always uses their catchphrase when they say something.
```python
class CoolLecturer(Lecturer):
	def __init__(self, fav_phrase):
		self.fav_phrase = fav_phrase
	def say(self, stuff):
		super.say(stuff + self.fav_phrase) # recall super() method
```
Recall [[Inheritance#`super()` method Going up one level]]
> **Question:** Aren't there two `say` methods in `CoolLecturer`? One in its own definition, and one in the superclass `Speaker`?

```python
ben = CoolLecturer("... how cool is that?")
ben.say("We will have PE tomorrow") # => We will have a PE tomorrow... how cool is that?
ben.lecture("CS1010S is fun")
# CS1010S is fun... how cool is that?
# You should take notes
```