# Pandas

Pandas is an open-source data manipulation and analysis library for Python. It provides easy-to-use data structures and functions for working with structured data, making it a powerful tool for data cleaning, exploration, and analysis. Pandas is widely used in data science, machine learning, and data analysis projects.

## Where is Pandas Used?

Pandas is used in various fields and industries for data manipulation and analysis. Some common applications of Pandas include:

- Data cleaning and preparation
- Data analysis and visualization
- Time series analysis
- Statistical analysis
- Data transformation and aggregation
- Working with structured data such as CSV files, Excel spreadsheets, SQL databases, and more

## Installing Pandas

To install Pandas, you need to have Python installed on your system. You can install Pandas using the Python package manager, `pip`. Open your command-line interface (e.g., Terminal on macOS, Command Prompt on Windows) and run the following command:

```markdown
pip install pandas
```

This command will download and install the Pandas library and its dependencies.

## Using Pandas

Once you have Pandas installed, you can start using it in your Python projects. Here are some common tasks and how to perform them using Pandas:

### Importing Pandas

To use Pandas in your Python script or Jupyter Notebook, you need to import it:

```python
import pandas as pd
```

### Creating a DataFrame

A DataFrame is a core data structure in Pandas. It's like a table with rows and columns. You can create a DataFrame from various data sources, such as lists, dictionaries, or external files (e.g., CSV, Excel).

```python
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}

df = pd.DataFrame(data)
```

### Loading Data from a File

You can load data from external files using Pandas. For example, to load data from a CSV file:

```python
df = pd.read_csv('data.csv')
```

### Data Exploration

You can explore your data by using various methods:

```python
# Display the first few rows of the DataFrame
df.head()

# Get summary statistics
df.describe()

# Select specific columns
df['Column_Name']

# Filter data based on conditions
df[df['Age'] > 30]
```

### Data Manipulation

Pandas provides numerous functions for data manipulation, such as:

```python
# Adding a new column
df['Salary'] = [50000, 60000, 75000]

# Removing a column
df.drop('Salary', axis=1, inplace=True)

# Sorting data
df.sort_values(by='Age', ascending=False)

# Grouping and aggregation
df.groupby('Age').mean()
```

### Data Visualization

Pandas can work seamlessly with other Python libraries like Matplotlib and Seaborn for data visualization.

```python
import matplotlib.pyplot as plt

# Plotting data
df.plot(x='Name', y='Age', kind='bar')
plt.show()
```

### Saving Data

After performing data analysis, you may want to save your results to a file.

```python
df.to_csv('output.csv', index=False)
```

These are just some of the basic operations you can perform with Pandas. The library offers a wide range of functionality, making it an essential tool for data analysis in Python.

For more detailed information, you can refer to the official [Pandas documentation](https://pandas.pydata.org/docs/).

## Pandera

`pip install pandera`

To install pandera.

## Pandas Topics Covered

- Series
- Pandera Types
- list,nested list and dictionary series
- DataFrames
- Pandas read json and html format
- DataFrame Schema
- DataFrame Operations
- Creating csv file using pandas

## Pandas DataFrame operations

- add new column
- 1. one column
- 2. two or more column
- delete column
- change data type of column
- map
- apply
- 1. on one column
- 2. more than one column
- concatenate
- 1. axis
      - 1. axis = 0 (top to bottom)
      - 2. axis = 1 (left to right)
- describe dataframe
- 1. `df.info()` # total index, columns names and data type, total fill cells
- 2. `df.describe()` # mean std, min # statistical properties | apply only numeric columns

## Apply operations on columns

- Extract one column from DataFrame
  - `dataframe['column']`
    - add new column to DataFrame
    - get column with space between columns text `column name`
  - `dataframe.column`
    - cannot add column to DataFrame
    - cannot access column with text space
- Extract two or more columns from DataFrame
  - `dataframe['column1','column2']`
    - pass list into DataFrame
- Delete Column
- Apply Arithmetic operations
