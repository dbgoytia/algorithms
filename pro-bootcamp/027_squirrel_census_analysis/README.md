# Central Park Squirrel Census

Back in 2018, some volunteers went into NY Central Park to get some metadata
around **squirrels**. Fun! I know. We will be using the data that this volunteers
gathered, and get some data analysis fun with it.

# Goals:

1. Find how many colours of squirrel are there (gray, cinammon, black)? Output
this into squirrel_count.csv using a Pandas DataFrame.

```
Number of squirrels per colour: 
 Primary Fur Color
Black        103
Cinnamon     392
Gray        2473
Name: X, dtype: int64
```

2. Find distribution of squirrels by age

```
Age distribution of squirrels: 
 Age
Adult       2568
Juvenile     330
Unknown      125
Name: X, dtype: int64
```

3. Find the squirrels activity

```
Activity of squirrels is: 
    Activity  Count
0   Running    730
1   Chasing    279
2  Climbing    658
3    Eating    760
4  Foraging   1435
```

4. Find the squirrels activity per shift

```
Activity of squirrel per shift is: 
        Running  Chasing  Climbing  Eating  Foraging
Shift                                              
AM         327      131       340     296       601
PM         403      148       318     464       834
```

