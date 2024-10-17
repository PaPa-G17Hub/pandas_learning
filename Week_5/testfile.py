import pandas as pd
import numpy as np

# print (pd)
languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])
positions = pd.Series([3,1,2,4])

# print(languages)
# print()
# print(positions)
# print()

# df = pd.DataFrame([("Anne",30),("Bill",27),("Charlie",55)])
# print(df)
# print()

# df2 = pd.DataFrame([("Anne",30),("Bill",27),("Charlie",55)], columns=["Name", "Age"])
# print(df2)

# Using a dictionary, with a key, value pair, to manually build a new dataframe
# df3 = pd.DataFrame({
#     "Languages": languages,
#     "Ranking": positions

# })

# print()
# print(df3)
# # print()

# # Using the concat method to automatically create a dataframe using two pandas
# df4 = pd.concat([languages, positions])
# print()
# print(df4)
# print()

# # using the "axis=1" parameter will display the data side by side, like a table. 
# # The default is "axis=0" and will display the data on 
# df5 = pd.concat([languages, positions], axis=1)
# print()
# print(df5)
# print()

# # using the column PROPERTY to provide descriptive headers
# df6 = pd.concat([languages, positions], axis=1)
# df6.columns = ["Languages", "Ranking"]
# print()
# print(df6)
# print()

# # Loading an external csv file into a panda dataframe
# df7 = pd.read_csv("Week_5\speeds.csv")
# print()
# print(df7)
# print()

# # Install the excel library needed to work with pandas
# pip install openpyxl

# Loading an external excel file into a panda dataframe
df8 = pd.read_excel("Week_5\speeds.xlsx")
print()
print(df8)
print()
