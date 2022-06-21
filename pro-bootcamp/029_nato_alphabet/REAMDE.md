# Basics around list comprehensions in Python3



## Python sequences

Python sequences (list, range, string, touple) they have a specific order.

The formula is easy to remember:

```
# structure of a list comprehension
new_var = [new_item for item in list] 
```


### Working with lists
Add +1 to each of the numbers in the list:

```
>>> a = [1,2,3]
>>> b = [ n+1 for n in a]
>>> b
[2, 3, 4]
```


Get only even numbers from a list

```
>>> even_nums_in_range = [n for n in range(1, 11) if n % 2 == 0]
>>> even_nums_in_range
[2, 4, 6, 8, 10]
```

### Working with strings
Store each letter as a value of a list:
```
>>> name ='Diego'
>>> spelling_bee=[ letter for letter in name ]
>>> spelling_bee
['D', 'i', 'e', 'g', 'o']
```

### Working with ranges
Square each value in the range(1,5)

```
>>> squared_values = [ x*x for x in range(1,5)]
>>> squared_values
[1, 4, 9, 16]
```

### Conditional list comprehensions

Formula:

```
new_list = [ new_item for item in list if test]
```

Find all names with less than four letters
```
>>> names
['Alex', 'Guill', 'Diego', 'Javier']
>>> short_names = [ name for name in names if len(name) < 5 ]
>>> short_names
['Alex']
```

Create a list that contains the names longer than 5 characters long, and all in caps.
```
>>> names = ['Alex', 'Guill', 'Diego', 'Javier']
>>> names
['Alex', 'Guill', 'Diego', 'Javier']
>>> long_names_caps = [ name.upper() for name in names if len(name) > 5 ]
>>> long_names_caps
['JAVIER']
```
