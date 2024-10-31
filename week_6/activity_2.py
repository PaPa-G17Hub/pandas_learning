# Download cleaning_activity.xlsx from Teams.
# Ensure this data is clean and accurate.

import pandas as pd

# read the excel file into a panda dataframe
df = pd.read_excel("cleaning_activity.xlsx")

print("\nReplace the index with the Transaction ID")
df = df.set_index("Transaction ID")

print("\nDrop the unnecesary column")
df = df.drop(columns=["Till ID"])

print("\nDrop the rows with nonsence data")
df = df.dropna(how="any")

print("\nDrop duplicate rows")
df = df.drop_duplicates()

print("\nFix any obvious outlier data")
print("\nTransaction ID = 56.0 has an eroneous value")
df.at[56.0,"Cost"] = 6.00
print("Transaction ID = 60.0 has no items in the basket and no cost")
df = df.drop([60.0])
print(df)

print("\nExplode the basket column and save in a new dataframe")

print("\nRemove the brackets and quotes from the Basket column")
df["Basket"] = df["Basket"].str.replace("'", "")
df["Basket"] = df["Basket"].str.replace("[", "")
df["Basket"] = df["Basket"].str.replace("]", "")
print(df["Basket"])

# def split_basket(basket_items):
#     items = basket_items.split(",")
#     stripped_items = [item.strip() for item in items]
#     return stripped_items

# df["Basket"] = df["Basket"].apply(split_basket)
# print(df["Basket"])