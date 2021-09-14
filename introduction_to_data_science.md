Course | Tags | Course link |
--------|:----:|:------------:|
**Introduction to Data Science in Python**| Python, pandas | https://learn.datacamp.com/courses/introduction-to-data-science-in-python |

**Solutions for chapters**

### 1. Getting Started in Python
* ##### **Exercise:** Importing Python modules
```python
# Use an import statement to import statsmodels
import statsmodels

# Import statsmodels under the alias sm
import statsmodels as sm

# Use an import statement to import seaborn with alias sns
import seaborn as sns
```
* ##### **Exercise:** Correcting a broken import
```python
# Fix the import of numpy to run without errors
import numpy as np
```
* ##### **Exercise:** Creating a float
```python
# Fill in Bayes' age (4.0)
bayes_age = 4.0

# Display the variable bayes_age
print(bayes_age)
```
* ##### **Exercise:** Creating strings
```python
# Bayes' favorite toy
favorite_toy = "Mr. Squeaky"

# Bayes' owner
owner = "DataCamp"

# Display variables
print(favorite_toy)
print(owner)
```
* ##### **Exercise:** Correcting string errors
```python
# One or more of the following lines contains an error
# Correct it so that it runs without producing syntax errors
birthday = "2017-07-14"
case_id = 'DATACAMP!123-456?'
```
* ##### **Exercise:** Load a DataFrame
```python
# Import pandas
import pandas as pd

# Load the 'ransom.csv' into a DataFrame
r = pd.read_csv('ransom.csv')

# Display DataFrame
print(r)
```
* ##### **Exercise:** Correcting a function error
```python
# One or more of the following lines contains an error
# Correct it so that it runs without producing syntax errors

# Plot a graph
plt.plot(x_values, y_values)

# Display the graph
plt.show()
```
* ##### **Exercise:** Snooping for suspects
```python
# Define plate to represent a plate beginning with FRQ
# Use * to represent the missing four letters
plate = 'FRQ****'

# Define plate to represent a plate beginning with FRQ
# Use * to represent the missing four letters
plate = 'FRQ****'

# Call the function lookup_plate()
lookup_plate(plate)

# Define plate to represent a plate beginning with FRQ
# Use * to represent the missing four letters
plate = 'FRQ****'

# Call the function lookup_plate()
lookup_plate(plate)

# Call lookup_plate() with the keyword argument for color
lookup_plate(plate, color='Green')
```
### 2. Loading Data in pandas
* ##### **Exercise:** Loading a DataFrame
```python
# Import pandas under the alias pd
import pandas as pd

# Load the CSV "credit_records.csv"
credit_records = pd.read_csv("credit_records.csv")

# Display the first five rows of credit_records using the .head() method
print(credit_records.head())
```
* ##### **Exercise:** Inspecting a DataFrame
```python
#Use .info() to inspect the DataFrame credit_records
print(credit_records.info())
```
* ##### **Exercise:** Two methods for selecting columns
```python
# Select the column item from credit_records
# Use brackets and string notation
items = credit_records.loc[:,'item']

# Display the results
print(items)

# Select the column item from credit_records
# Use dot notation
items = credit_records.item

# Display the results
print(items)
```
* ##### **Exercise:** Correcting column selection errors
```python
# One or more lines of code contain errors.
# Fix the errors so that the code runs.

# Select the location column in credit_records
location = credit_records['location']

# Select the item column in credit_records
items = credit_records.item

# Display results
print(location)
```
### 3. Plotting Data with matplotlib
### 4. Different Types of Plots
