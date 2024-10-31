import pandas as pd

df = pd.read_csv("results.csv")
# print the entire dataframe
# print(df)

# We can see the number of rows, the column numbers and the column names.
# Non-Null Count shows us how many values are not “null” values.

# print("\nShow the number of rows, the column numbers and the column names.")
# df.info()

# print("\nShow df.describe()")
# print(df.describe())

# print("\nCount shows us how many values are in the column.")
# print("\nMean is the average number of goals scored at home and away.\nThey’re quite similar, but it suggest home teams might score more goals.")
# print("\n")

# print(df["home_score"].value_counts(normalize=True) * 100)

# a boolean series that returns true for the rows that are less then 5
mask = print(df["home_score"] < 5)
masked_df = df[mask]

# print(masked_df)

# pip install ydata-profiling