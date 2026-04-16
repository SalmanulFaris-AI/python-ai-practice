import pandas as pd

# Create DataFrame
data = [
    ["apple", "yes", 10],
    ["banana", "yes", 7],
    ["orange", "no", 5]
]

df = pd.DataFrame(data, columns=["fruit_name", "in_stock", "price"])

print("Original Data:")
print(df)

# Sorting
print("\nSorted by index (descending):")
print(df.sort_index(ascending=False))

print("\nSorted by price:")
print(df.sort_values(by="price"))

# Set index
df2 = df.set_index("fruit_name")

print("\nData with fruit_name as index:")
print(df2)

# Accessing data
print("\nSingle column:")
print(df2["price"])

print("\nMultiple columns:")
print(df2[["in_stock", "price"]])

# iloc (position-based)
print("\nUsing iloc:")
print(df.iloc[0])         # first row
print(df.iloc[:, 1])      # second column

# loc (label-based)
print("\nUsing loc:")
print(df2.loc["banana"])  # row by label
print(df2.loc[["apple", "orange"], ["price"]])

# Filtering
print("\nPrice > 6:")
print(df[df["price"] > 6])

print("\nPrice > 6 (only in_stock):")
print(df.loc[df["price"] > 6, "in_stock"])
