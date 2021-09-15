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
----
# Define plate to represent a plate beginning with FRQ
# Use * to represent the missing four letters
plate = 'FRQ****'

# Call the function lookup_plate()
lookup_plate(plate)
----
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
* ##### **Exercise:** More column selection mistakes
```python
# Use info() to inspect mpr
print(mpr.info())
----
# Use info() to inspect mpr
print(mpr.info())

# The following code contains one or more errors
# Correct the mistakes in the code so that it runs without errors

# Select column "Dog Name" from mpr
name = mpr.loc[:,"Dog Name"]

# Select column "Missing?" from mpr
is_missing = mpr.loc[:, 'Missing?']

# Display the columns
print(name)
print(is_missing)
```
* ##### **Exercise:** Logical testing
```python
# Is height_inches greater than 70 inches?
print(height_inches > 70)
----
# Is height_inches greater than 70 inches?
print(height_inches > 70)

# Is plate1 equal to "FRQ123"?
print(plate1 == "FRQ123")
----
# Is height_inches greater than 70 inches?
print(height_inches > 70)

# Is plate1 equal to "FRQ123"?
print(plate1 == "FRQ123")

# Is fur_color not equal to "brown"?
print(fur_color != "brown")
```
* ##### **Exercise:** Selecting missing puppies
```python
# Select the dogs where Age is greater than 2
greater_than_2 = mpr[mpr.loc[:,'Age'] > 2]
print(greater_than_2)

# Select the dogs whose Status is equal to Still Missing
still_missing = mpr[mpr.loc[:,'Status'] == 'Still Missing']
print(still_missing)

# Select all dogs whose Dog Breed is not equal to Poodle
not_poodle = mpr[mpr.loc[:,'Dog Breed'] != 'Poodle']
print(not_poodle)
```
* ##### **Exercise:** Narrowing the list of suspects
```python
# Select purchases from 'Pet Paradise'
purchase = credit_records[credit_records.loc[:,'location'] == 'Pet Paradise']

# Display
print(purchase)
```
### 3. Plotting Data with matplotlib
* ##### **Exercise:** Working hard
```python
# From matplotlib, import pyplot under the alias plt
from matplotlib import pyplot as plt
----
# From matplotlib, import pyplot under the alias plt
from matplotlib import pyplot as plt

# Plot Officer Deshaun's hours_worked vs. day_of_week
plt.plot(deshaun.loc[:,'day_of_week'], deshaun.loc[:,'hours_worked'])
plt.show()
----
# From matplotlib, import pyplot under the alias plt
from matplotlib import pyplot as plt

# Plot Officer Deshaun's hours_worked vs. day_of_week
plt.plot(deshaun.day_of_week, deshaun.hours_worked)

# Display Deshaun's plot
plt.show()
```
* ##### **Exercise:** Or hardly working?
```python
# Plot Officer Deshaun's hours_worked vs. day_of_week
plt.plot(deshaun.day_of_week, deshaun.hours_worked)

# Plot Officer Aditya's hours_worked vs. day_of_week
plt.plot(aditya.day_of_week, aditya.hours_worked)

# Plot Officer Mengfei's hours_worked vs. day_of_week
plt.plot(mengfei.day_of_week, mengfei.loc[:,'hours_worked'])

# Display all three line plots
plt.show()
```
* ##### **Exercise:** Adding a legend
```python
# Add a label to Deshaun's plot
plt.plot(deshaun.loc[:,'day_of_week'], deshaun.loc[:,'hours_worked'], label = 'Deshaun')

# Officer Aditya
plt.plot(aditya.loc[:,'day_of_week'], aditya.loc[:,'hours_worked'])

# Officer Mengfei
plt.plot(mengfei.day_of_week, mengfei.hours_worked)

# Display plot
plt.show()
----
# Officer Deshaun
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label='Deshaun')

# Add a label to Aditya's plot
plt.plot(aditya.day_of_week, aditya.hours_worked, label = 'Aditya')

# Add a label to Mengfei's plot
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label = 'Mengfei')

# Display plot
plt.show()
----
# Officer Deshaun
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label='Deshaun')

# Add a label to Aditya's plot
plt.plot(aditya.day_of_week, aditya.hours_worked, label='Aditya')

# Add a label to Mengfei's plot
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label='Mengfei')

# Add a command to make the legend display
plt.legend()

# Display plot
plt.show()
```
* ##### **Exercise:** Adding labels
```python
# Lines
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label='Deshaun')
plt.plot(aditya.day_of_week, aditya.hours_worked, label='Aditya')
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label='Mengfei')

# Add a title
plt.title('Work hours in a week')

# Add y-axis label
plt.ylabel('hours worked')

# Legend
plt.legend()
# Display plot
plt.show()
```
* ##### **Exercise:** Adding floating text
```python
# Create plot
plt.plot(six_months.month, six_months.hours_worked)

# Add annotation "Missing June data" at (2.5, 80)
plt.text(2.5, 80, 'Missing June data')

# Display graph
plt.show()
```
* ##### **Exercise:** Tracking crime statistics
```python
# Change the color of Phoenix to `"DarkCyan"`
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix", color = 'DarkCyan')

# Make the Los Angeles line dotted
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles", linestyle = ':')

# Add square markers to Philedelphia
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia", marker = 's')

# Add a legend
plt.legend()

# Display the plot
plt.show()
```
* ##### **Exercise:** Playing with styles
```python
# Change the style to fivethirtyeight
plt.style.use('fivethirtyeight')

# Plot lines
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix")
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles")
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia")

# Add a legend
plt.legend()

# Display the plot
plt.show()
----
# Change the style to ggplot
plt.style.use('ggplot')

# Plot lines
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix")
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles")
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia")

# Add a legend
plt.legend()

# Display the plot
plt.show()
----
# Choose any of the styles
plt.style.use('seaborn')

# Plot lines
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix")
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles")
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia")

# Add a legend
plt.legend()

# Display the plot
plt.show()
```
* ##### **Exercise:** Identifying Bayes' kidnapper
```python
# x should be ransom.letter and y should be ransom.frequency
plt.plot(ransom.loc[:,'letter'], ransom.loc[:,'frequency'],
         # Label should be "Ransom"
         label="Ransom",
         # Plot the ransom letter as a dotted gray line
         linestyle=':', color='gray')

# Display the plot
plt.show()
----
# Plot each line
plt.plot(ransom.letter, ransom.frequency,
         label='Ransom', linestyle=':', color='gray')

# X-values should be suspect1.letter
# Y-values should be suspect1.frequency
# Label should be "Fred Frequentist"
plt.plot(suspect1.loc[:,'letter'], suspect1.loc[:,'frequency'], label='Fred Frequentist')

# Display the plot
plt.show()
----
# Plot each line
plt.plot(ransom.letter, ransom.frequency,
         label='Ransom', linestyle=':', color='gray')
plt.plot(suspect1.letter, suspect1.frequency,
         label='Fred Frequentist')

# X-values should be suspect2.letter
# Y-values should be suspect2.frequency
# Label should be "Gertrude Cox"
plt.plot(suspect2.loc[:,'letter'], suspect2.loc[:, 'frequency'], label = 'Gertrude Cox')

# Display plot
plt.show()
----
# Plot each line
plt.plot(ransom.letter, ransom.frequency,
         label='Ransom', linestyle=':', color='gray')
plt.plot(suspect1.letter, suspect1.frequency, label='Fred Frequentist')
plt.plot(suspect2.letter, suspect2.frequency, label='Gertrude Cox')

# Add x- and y-labels
plt.xlabel("Letter")
plt.ylabel("Frequency")

# Add a legend
plt.legend()

# Display plot
plt.show()
```
### 4. Different Types of Plots
* ##### **Exercise:** Charting cellphone data
```python
# Explore the data
print(cellphone.head())

# Create a scatter plot of the data from the DataFrame cellphone
plt.scatter(cellphone.loc[:,'x'], cellphone.loc[:,'y'])

# Add labels
plt.ylabel('Latitude')
plt.xlabel('Longitude')

# Display the plot
plt.show()
```
* ##### **Exercise:** Modifying a scatterplot
```python
# Change the marker color to red
plt.scatter(cellphone.loc[:,'x'], cellphone.loc[:,'y'],
           color='red')

# Add labels
plt.ylabel('Latitude')
plt.xlabel('Longitude')

# Display the plot
plt.show()
----
# Change the marker shape to square
plt.scatter(cellphone.x, cellphone.y,
           color='red',
           marker='s')

# Add labels
plt.ylabel('Latitude')
plt.xlabel('Longitude')

# Display the plot
plt.show()
----
# Change the transparency to 0.1
plt.scatter(cellphone.x, cellphone.y,
           color='red',
           marker='s',
           alpha=0.1)

# Add labels
plt.ylabel('Latitude')
plt.xlabel('Longitude')

# Display the plot
plt.show()
```
* ##### **Exercise:** Build a simple bar chart
```python
# Display the DataFrame hours using print
print(hours)
----
# Display the DataFrame hours using print
print(hours)

# Create a bar plot from the DataFrame hours

plt.bar(hours.loc[:,'officer'], hours.avg_hours_worked)

# Display the plot
plt.show()
----
# Display the DataFrame hours using print
print(hours)

# Create a bar plot from the DataFrame hours
plt.bar(hours.officer, hours.avg_hours_worked,
        # Add error bars
        yerr=hours.std_hours_worked)

# Display the plot
plt.show()
```
* ##### **Exercise:** Where did the time go?
```python
# Plot the number of hours spent on desk work
plt.bar(hours.loc[:,'officer'], hours.desk_work,
label = "Desk Work")

plt.title('Desk Work')
# Display the plot
plt.show()
----
# Plot the number of hours spent on desk work
plt.bar(hours.officer, hours.desk_work, label='Desk Work')

# Plot the hours spent on field work on top of desk work
plt.bar(hours.officer, hours.field_work, bottom = hours.desk_work, label = 'Field Work')

# Add a legend
plt.legend()

# Display the plot
plt.show()
```
* ##### **Exercise:** Modifying histograms
```python
# Create a histogram of the column weight
# from the DataFrame puppies
plt.hist(puppies.loc[:,'weight'])

# Add labels
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show()
----
# Change the number of bins to 50
plt.hist(puppies.weight,
        bins=50)

# Add labels
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show()
----
# Change the range to start at 5 and end at 35
plt.hist(puppies.weight,range=(5,35))

# Add labels
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show()
```
* ##### **Exercise:** Heroes with histograms
```python
# Create a histogram of gravel.radius
plt.hist(gravel.loc[:,'radius'])

# Display histogram
plt.show()
----
# Create a histogram
# Range is 2 to 8, with 40 bins
plt.hist(gravel.radius, bins=40, range=(2,8))

# Display histogram
plt.show()
----
# Create a histogram
# Normalize to 1
plt.hist(gravel.radius,
         bins=40,
         range=(2, 8),
         density=True)

# Display histogram
plt.show()
----
# Create a histogram
plt.hist(gravel.radius,
         bins=40,
         range=(2, 8),
         density=True)

# Label plot
plt.xlabel('Gravel Radius (mm)')
plt.ylabel('Frequency')
plt.title('Sample from Shoeprint')

# Display histogram
plt.show()
```
