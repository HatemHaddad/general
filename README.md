# general
# For loop
* List
* Dictionary
* DataFrame

# Loop over list
```python
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
```

# Change for loop to use enumerate() and update print()
```python
for x,y in enumerate(areas) :
  print("room {}: {}".format(x,y))
```

# Loop over Dictionary
In Python 3, you need the **items()** method to loop over a dictionary:
```python
world = { "afghanistan":30.55, 
          "albania":2.77,
          "algeria":39.21 }

for key, value in world.items() :
    print(key + " -- " + str(value))
 ```
 
 # Loop over Numpy array
If you're dealing with a 1D Numpy array, looping over all elements can be as simple as:

```python
for x in my_array :
    ...
```
If you're dealing with a 2D Numpy array, it's more complicated. A 2D array is built up of multiple 1D arrays. To explicitly iterate over all separate elements of a multi-dimensional array, you'll need this syntax:

```python
for x in np.nditer(my_array) :
    ...
```

