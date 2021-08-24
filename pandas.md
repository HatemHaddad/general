
# Inspecting a DataFrame
When you get a new DataFrame to work with, the first thing you need to do is explore it and see what it contains. There are several useful methods and attributes for this.

>**.head()** returns the first few rows (the “head” of the DataFrame).
>
>**.info()** shows information on each of the columns, such as the data type and number of missing values.
>
>**.shape** returns the number of rows and columns of the DataFrame.
>
>**.describe()** calculates a few summary statistics for each column.


# Parts of a DataFrame
To better understand DataFrame objects, it's useful to know that they consist of three components, stored as attributes:

>**.values**: A two-dimensional NumPy array of values.
>
>**.columns**: An index of columns: the column names.
>
>**.index**: An index for the rows: either row numbers or row names.

You can usually think of indexes as a list of strings or numbers, though the pandas Index data type allows for more sophisticated options. 