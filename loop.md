
# For loop
* List
* Dictionary
* DataFrame

# List
Using a for loop to iterate over a list only gives you access to every list element in each run, one after the other. If you also want to access the index information, so where the list element you're iterating over is located, you can use **enumerate()**.

As an example, have a look at how the for loop from the video was converted:

```python
fam = [1.73, 1.68, 1.71, 1.89]
for index, height in enumerate(fam) :
    print("person " + str(index) + ": " + str(height))
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

