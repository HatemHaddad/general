# Create a series object from a python list

we use a Series method under the category constucter methods as it creates a series.

Series can have an index other than numbers - better than a list
Pandas generates a numerical index as a default for the series

```python
ice_cream = ['Chocolate','Vanilla','Strawberry','Rum raisin']

pd.Series(ice_cream)
```

# Create a series object from a python dictionary

The index of a dictionary is the key
The index can have duplicate ( not unique ) keys and not like a dictionary which cant be duplicated ( unique )

```python
webster = { 'Ardvark' : 'An animal',
            'Banana' : 'A delicious fruit',
             'Cyan' :'A color'}
pd.Series(webster)
```

# Intro to Attributes

Objects is python have attributes and methods

A pandas series is just one type of objects

**Attributes** gives information about an object,attributes do not modify an object
**Methods** do operate on an object, manipualatin or calculation

```python
about_me =['Handsome','Brilliant','Charming','Humble']
s = pd.Series(about_me)

s.values # an array of values
s.index # range index
s.dtype

# think of it as a puzzle and we look at the different pieces
```

# Intro to Methods

Methods do change an object

```python
prices =[2.99, 3.45,1.36]
s = pd.Series(prices)

s.sum()
s.product()
s.mean()
```
