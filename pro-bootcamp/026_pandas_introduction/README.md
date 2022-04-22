# Pandas introduction

The goal to day is to get a first hands-on approach with Pandas.

# Main Pandas data structures
* Series: A series is a 1-dimensional structure, homogeneously-typed array.
* DataFrames: A 2-D array holding data, size-mutable tabular structure with poitentially heterogeneously-typed column.


The best way to think about this is that a DataFrame, is a container for Series, and Series
is a container for scalars. It is ordered this way so we can insert and remove objects from
these containers in a dictionary-like fashion.

All Pandas data structures are value-mutable, but not always size-mutable.

# Example

In this example we parse the data using plain "open" command, the bult-in "csv" library,
and "pandas", to identify the difference.

## With plain open
With plain open, you can see that the data needs a lot of cleanup and extra steps to be usable,
making it a bit hard to work on:
```
['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']
```

## With CSV built-in library

With this one it starts to feel a little bit better, you can see that the output is already
in the form of a list and it's very easy to use. However, you still need to have thorough
understanding of what the data is representing, for example, if we were to take only the
'Conditions' for the last 7 days, we would need to know tha the condition is stored on the position [2]
of the data structure returned.

We also have to skip the first line always, making it a bit cumbersome.

```
[['day', 'temp', 'condition'], ['Monday', '12', 'Sunny'], ['Tuesday', '14', 'Rain'], ['Wednesday', '15', 'Rain'], ['Thursday', '14', 'Cloudy'], ['Friday', '21', 'Sunny'], ['Saturday', '22', 'Sunny'], ['Sunday', '24', 'Sunny']]
```

## With Pandas
Now enter the world of Pandas, it is way much more intelligent than the previous two examples.
if you see the output, you'll notice that you already get it very well formatted. 


```
         day  temp condition
0     Monday    12     Sunny
1    Tuesday    14      Rain
2  Wednesday    15      Rain
3   Thursday    14    Cloudy
4     Friday    21     Sunny
5   Saturday    22     Sunny
6     Sunday    24     Sunny
```

Pandas will also automatically know (when parsing csv) that the first column represents the name 
of the column, so you can very easily do something like data['temp'] to print only the temp column.
It's also very smart at guessing the type of the **series**.

```
0    12
1    14
2    15
3    14
4    21
5    22
6    24
Name: temp, dtype: int64
```

You can also do very cool things like converting DataFrames it to various formats out of the box, for example,
you can conver this automatically to dictionaries and start working with it like so:
```
data_dict = data.to_dict()
<class 'dict'>
{'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}
```

Very similarly, you can move all Series to Python lists out of the box:
```
<class 'list'>
[12, 14, 15, 14, 21, 22, 24]
```

# References
* https://pandas.pydata.org/docs/getting_started/overview.html