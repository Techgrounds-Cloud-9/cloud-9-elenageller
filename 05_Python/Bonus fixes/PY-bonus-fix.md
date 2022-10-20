
## Exercise 1

'''
The output should be:
hello Casper
hello Floris
hello Esther
'''
foo = 'hello'
ls = ['Casper', 'Floris', 'Esther']
for name in ls:
	print(loo,name)

## Result

``` python
foo = 'hello'
ls = ['Casper', 'Floris', 'Esther']
for name in ls:
	print(foo,name)
```

## Exercise 2

'''
The output should be:
100
'''
foo = 20
bar = '80'
print(foo + bar)

## Result

``` python
foo = 20
bar = '80'
print(foo + int(bar))
```

## Exercise 3

'''
The output should be:
30
'''
foo = 20
for i in range(10):
	foo += 1

print(foo)

## Result

``` python
foo = 20
for i in range(10):
	foo += 1

print(foo)
```

## Exercise 4

'''
The output should be:
there are 0 kids on the street
there are 1 kids on the street
there are 2 kids on the street
there are 3 kids on the street
there are 4 kids on the street
'''
foo = 0
while foo <= 5:
	print('there are', foo, 'kids on the street')
	foo += 1

## Result

	```python
	foo = 0
while foo < 5:
	print('there are', foo, 'kids on the street')
	foo += 1

	```

## Exercise 5

'''
The output should be:
Star Wars
'''
ls = ['Lord of the rings', 'Star Trek', 'Iron Man', 'Star Wars']
print(ls[4])

## Result

```python

ls = ['Lord of the rings', 'Star Trek', 'Iron Man', 'Star Wars']
print(ls[3])

```

## Exercise 6

'''
The output should be:
80
'''
foo = 80
if foo < 30:
	print(foo)
else:
	print('big number wow')
elif foo < 100:
	print(foo)

## Result

```python
foo = 80
if foo < 30:
	print(foo)
elif foo < 100:
	print(foo) 
else:
	print('big number wow')
	```

## Exercise 7

'''
The output should be:
['Dog', 'Cat', 'Fly']
'''
ln = ['Dog', 'Cat', 'Elephant', 'Fly', 'Horse']
short_names = []

for animal in ln:
	if len(animal) == 3:
		short_names.append(animal)
	short_names = []

print(short_names)

## Result

```python
ln = ['Dog', 'Cat', 'Elephant', 'Fly', 'Horse']
short_names = []

for animal in ln:
	if len(animal) == 3:
		short_names.append(animal)

print(short_names)
```

## Exercise 8

'''
The output should be:
20
'''
foo = 10
bar = 2
print(foo * bar)

## Result

```python
foo = 10
bar = 2
print(foo * bar)
```

## Exercise 9

'''
The output should be:
0
1
2
3
4
8
9
'''
for i in range(10):
	if i < 5:
		print(i)
	elif i < 8:
		break
	else:
		print(i)

## Result

```python
for i in range(10):
	if i < 5:
		print(i)
	elif i < 8:
		continue
	else:
		print(i)
		```

## Exercise 10

'''
The output should be:
the number is 20
'''
print('the number is' + 20)

## Result

```python
print('the number is ' + str(20))
```

## Exercise 11

'''
The output should be:
IT LIVES!
'''
dev monster():
	print('IT LIVES!')

monster()

## Result

```python
def monster():
	print('IT LIVES!')

monster()
```

## Exercise 12

'''
The output should be:
4
16129
'''
def square(x):
	return x**2

nr = square(2)
print(nr)

big = square(foo)
print(big)

foo = 127

## Result

```python

foo = 127

def square(x):
	return x**2

nr = square(2)
print(nr)

big = square(foo)
print(big)
```

## Exercise 13

'''
The output should be:
Your random number is: <insert random number here>
'''
import random

random.randint(1,100)
print("Your random number is:")

## Result

```python
import random

x= random.randint(1,100)
print("Your random number is: " + str(x))
```

## Exercise 14

'''
The output should be:
True
'''
def rtn(x):
	return(x)

foo = rtn(3)

if foo > rtn(4):
	print(True)
else:
	print(False)

## Result

```python
def rtn(x):
	return(x)

foo = rtn(3)

if foo < rtn(4):
	print(True)
else:
	print(False)
	```

## Exercise 15

'''
The output should be:
a5|||5|||5|||a5|||5|||5|||a5|||5|||5|||
'''
foo = ''
for i in range(3):
	foo += 'a'
	for j in range(3):
		foo += '5'
	for k in range(3):
		foo += '|'

print(foo)

## Result

```python
foo = ''
for i in range(3):
	foo += 'a'
	for j in range(3):
		foo += '5'
	    for k in range(3):
		    foo += '|'

print(foo)
```

## Exercise 16

'''
The output should be:

'''
import random

# generate random int
goal = random.randint(1,100)

win = False
tries = 0

while win == False and tries < 7:
	try:
		# ask for input
		inpt = int(input("Please input a number between 1 and 100: "))
		# count attempt as a try
		tries += 1

		# check for match
		if inpt == goal:
			win = True
			print("Congrats, you guessed the number!")
			print("It took you", tries, "tries")
		# give hints
		elif inpt < goal:
			print("The number should be higher")
		else:
			print("The number should be lower")

	except:
		print("Please type an integer")

# 
if win == False:
	print("Game over! You took more than seven tries")

## Result

```python
import random

# generate random int
goal = random.randint(1,100)

win = False
tries = 0

while win == False and tries < 7:
	try:
		# ask for input
		inpt = int(input("Please input a number between 1 and 100: "))
		# count attempt as a try
		tries += 1

		# check for match
		if inpt == goal:
			win = True
			print("Congrats, you guessed the number!")
			print("It took you", tries, "tries")
		# give hints
		elif inpt < goal:
			print("The number should be higher")
		else:
			print("The number should be lower")

	except:
		print("Please type an integer")

if win == False:
	print("Game over! You took more than seven tries")
	```