## 1 Transforming DataFrames

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

# Sorting rows
Finding interesting bits of data in a DataFrame is often easier if you change the order of the rows. You can sort the rows by passing a column name to **.sort_values()**.

In cases where rows have the same value (this is common if you sort on a categorical variable), you may wish to break the ties by sorting on another column. You can sort on multiple columns in this way by passing a list of column names.

# Sort on 
* **one column**	df.sort_values("col",ascending=True)
* **multiple columns**	df.sort_values(["col1", "col2"],ascending=[True,False])

By combining **.sort_values() with .head()**, you can answer questions in the form, "What are the top cases where…?".

# Subsetting columns
When working with data, you may not need all of the variables in your dataset. Square brackets ([]) can be used to select only the columns that matter to you in an order that makes sense to you. To select only "col_a" of the DataFrame df, use

df["col_a"]

To select "col_a" and "col_b" of df, use

df[["col_a", "col_b"]]

# Subsetting rows
A large part of data science is about finding which bits of your dataset are interesting. One of the simplest techniques for this is to find a subset of rows that match some criteria. This is sometimes known as filtering rows or selecting rows.

There are many ways to subset a DataFrame, perhaps the most common is to use relational operators to return True or False for each row, then pass that inside square brackets.
```python
dogs[dogs["height_cm"] > 60]
dogs[dogs["color"] == "tan"]
```
You can filter for multiple conditions at once by using the "bitwise and" operator, &.
```python
dogs[(dogs["height_cm"] > 60) & (dogs["color"] == "tan")]
```

# Subsetting rows by categorical variables
Subsetting data based on a categorical variable often involves using the "or" operator (|) to select rows from multiple categories. This can get tedious when you want all states in one of three different regions, for example. Instead, use the **`.isin()`** method, which will allow you to tackle this problem by writing one condition instead of three separate ones.
```python
colors = ["brown", "black", "tan"]
condition = dogs["color"].isin(colors)
dogs[condition]
```

# Adding new columns
You aren't stuck with just the data you are given. Instead, you can add new columns to a DataFrame. This has many names, such as transforming, mutating, and feature engineering.

You can create new columns from scratch, but it is also common to derive them from other columns, for example, by adding columns together or by changing their units.

# 2 Aggregating DataFrames

## Mean and median
Summary statistics are exactly what they sound like - they summarize many numbers in one statistic. For example, mean, median, minimum, maximum, and standard deviation are summary statistics. Calculating summary statistics allows you to get a better sense of your data, even if there's a lot of it.
```python
# Print the mean of weekly_sales
print(sales['weekly_sales'].mean())

# Print the median of weekly_sales
print(sales['weekly_sales'].median())
```
