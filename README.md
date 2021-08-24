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
In Python 3, you need the items() method to loop over a dictionary:
```python
world = { "afghanistan":30.55, 
          "albania":2.77,
          "algeria":39.21 }

for key, value in world.items() :
    print(key + " -- " + str(value))
 ```

