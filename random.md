# Random float
Randomness has many uses in science, art, statistics, cryptography, gaming, gambling, and other fields. 

All the functionality you need is contained in the `random` package, a sub-package of `numpy`. 

**seed()**: sets the random seed, so that your results are reproducible between simulations. As an argument, it takes an integer of your choosing. If you call the function, no output will be generated.

**rand()**: if you don't specify any arguments, it generates a random float between **zero** and **one**.

```python
# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())
```
# Roll the dice
Use **randint()**, also a function of the random package, to generate integers randomly. The following call generates the integer 4, 5, 6 or 7 randomly. 8 is not included.

```python
import numpy as np
np.random.randint(4, 8)
```
