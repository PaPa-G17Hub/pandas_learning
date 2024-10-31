import pandas as pd
import numpy as np

languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])
positions = pd.Series([3,1,2,4])

# Using a dictionary, with a key, value pair, to manually build a new dataframe
df3 = pd.DataFrame({
    "Languages": languages,
    "Ranking": positions

})

# adding a row with values to the end of the dataframe using the location property
df3.loc[4] = ["PHP", 11]

print("Original data")
print(df3)
print()

# # adding a row with values to the middle of the dataframe using the location property with an intermediate location value
# df3.loc[3.5] = ["KESL", 20]

# print()
# print(df3)
# print()

# # sorting the dataframe will now position the rows in numerical order
# df3 = df3.sort_index()

# print()
# print(df3)
# print()

# # # resetting the dataframes index will make it more natural, but will keep the original index for reference
# df3 = df3.reset_index()

# print()
# print(df3)
# print()

# # we can remove the orginal index with the drop keyword
# df3 = df3.reset_index(drop=True)

# print()
# print(df3)
# print()

# df4 = pd.DataFrame({
#     "Languages": ["PHP"],
#     "Ranking": [11]
# })
# print()
# print(df4)
# print()

# # This will have multiple indexes[0]
# df5 = pd.concat([df3,df4])
# print()
# print(df5)
# print()

# # This will have proper indexes[0]
# df6 = pd.concat([df3,df4], ignore_index=True)
# print()
# print(df6)
# print()

# adding new rows to the original dataframe using the concat method 
df7 = pd.DataFrame({
    "Languages": ["Java", "TypeScript"],
    "Ranking": [7, 5]
})
print("Create a new dataframe with two new languages")
print(df7)
print()


# This will have proper indexes[0]
df8 = pd.concat([df3,df7], ignore_index=True)
print("Adding these new languages to the 2023 rankings")
print(df8)
print()

# adding a new column to the original dataframe
df8["Ranking 2022"] = [4,1,2,3,10,6,5]
print("Dataframe 8")
print(df8)
print()

# adding a new column using the concat method
new_column = pd.DataFrame({
    "Ranking 2022": [4,1,2,3,10,6,5]
})

df9 = pd.concat([df8,new_column], axis=1)

print("Dataframe 9")
print(df9)
print()

# adding a new column to the original dataframe
df9["Ranking 2020"] = [4,1,2,3,10,6,5]
print("Dataframe with 2020 data")
print(df9)
print()

# adding a new column using the concat method
new_column_2 = pd.DataFrame({
    "Ranking 2019": [4,1,2,3,10,6,5]
})

df11 = pd.concat([df9,new_column_2], axis=1)
print("Dataframe with 2019 data")
print(df9)
print()

df11.insert(3, "Ranking 2021", [3,1,2,4,11,5,7])
print("Dataframe with 2021 data")
print(df11)
print()


# amending a column name. using the inplace keyword will modify the existing dataframe instead of creating a new one
df11.rename(columns={"Ranking" : "Ranking 2023"}, inplace=True)
print("Modifying the column name")
print(df11)
print()

# use the languages as the index
df12 = df11.set_index("Languages")
print("Using the Language column as the index")
print(df12)
print()

