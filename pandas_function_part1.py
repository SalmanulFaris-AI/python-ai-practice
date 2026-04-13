import pandas as pd

# Create DataFrame
data = [
    ["apple", "yes", 10],
    ["banana", "yes", 7],
    ["orange", "no", 5]
]

df = pd.DataFrame(data, columns=["fruit_name", "in_stock", "price"])

# Basic info
print(df)
print("\nInfo:")
df.info()

# Data types
print("\nData Types:")
print(df.dtypes)

# Values and columns
print("\nValues:")
print(df.values)

print("\nColumns:")
print(df.columns)

# Describe
print("\nDescribe (numeric):")
print(df.describe())

print("\nDescribe (all):")
print(df.describe(include='all'))

# Index operations
print("\nSet index:")
print(df.set_index("fruit_name"))

print("\nReset index:")
print(df.reset_index())

# Column access
print("\nFruit names:")
print(df["fruit_name"])

# Unique values
print("\nUnique in_stock values:")
print(df["in_stock"].unique())
