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
# Parameters and Arguments

Methods have something called Parametrs and Parameters take values called Arguments

```python
# Lets take a video game as an example
# Think about the options and setting the game may have
# Difficulty - Easy, Medium, Hard --- A setting
# Volume - 1 through 10
# Subtitles - True / False
#
# In programming, the option itself( Difficulty ) is the Parameter
# The option that we select ( Easy ) from the choices is the Argument
# Easy is the Argument that we are proving to the Difficulty Parameter
# Parameter is the name of the option and the Argument is the choice that we choose for that option

fruits = ['Apple', 'Orange', 'Plum', 'Grapes', 'Blueberry','Watermelon']
weekdays =['Monday','Tuesday','Wednesday','Thursday','Friday','Monday']

pd.Series(# click here shift+tab and we will get the documentation)

# We will see the Parameters and = sign with the values. These values are the default argument that pandas use as default

pd.Series(fruits,weekdays) # implicit ordering as it figures the parameters by its location = feeding the arguments sequentially 
pd.Series(data = fruits, index = weekdays) # explicit ordering as it figures the parameter by its name
pd.Series(fruits, index = weekdays) # mix - first argument sequentially and other argument expicit

# index in series should not be unique
```

# Import Series withn the .read_csv() Method

```python
pd.read_csv("file.csv",usecols=['col'],squeeze=True) 
# pandas import a file as a DataFrame even if it is one colums. 
# We used squeeze parameter to save it as Series
```
# The .head() and .tail() Method

```python
df.head()
df.tail()
# This is a new dataframe that shows the first and last n rows
```
# Python Built-In Functions

The normal python functions work well with Series object

```python
len(pokemon) # display the length of the series

type(pokemon) # displays the type of an object

dir(pokemon)# shows all the available attributes and methods

sorted(pokemon) # sorted list of a series

list(pokemon) # a list from a series

dict(pokemon) # a dictionar from a series. Then index will be the key

max(pokemon)

min(pokemon)
```
# More Series Attributes

```python

pokemon.is_unique # shows if the values are unique

pokemon.ndim # number of dimension. For series it is 1

pokemon.shape 

pokemon.size # tolal number of items. It counts null items

pokemon.name # shows the header name.

pokemon.name ='Pokemon Master' # changes the name
```

# The .sort_values() Method

```python
pokemon.sort_values(ascending=False)
```


