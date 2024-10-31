# Use .loc[] to produce the same results pictured.

# Remember :
# df.loc[start:stop:step, start:stop:step]
#         row             column

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
print("Adding rankings for 2022")
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

print(df12.loc["Python":"HTML":1,"Ranking 2023":"Ranking 2019":2])

print("\nHTML , Ranking 2023")
print(df12.loc["HTML","Ranking 2023"])

print("\nSQL , Ranking 2021")

print(df12.iloc[3,2])

print("\nHTML , Ranking 2023")
print(df12.at["HTML","Ranking 2023"])

print(df12.head(2))