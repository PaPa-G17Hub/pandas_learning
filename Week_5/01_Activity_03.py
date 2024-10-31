# Amend your solar system dataframe to
# add:
# • Who discovered each planet
# • The year it was discovered
# • Elements of its composition

import pandas as pd
import numpy as np
planet_name = pd.Series(["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"])
planet_average_temperature = pd.Series([167, 464, 15, -65, -110, -140, -195, -200])
planet_radius = pd.Series([2439.7, 6051.8, 6371, 3389.5, 69911, 58232, 25362, 24622])
planet_colour = pd.Series(["Gray", "Yellow", "Blue", "Red", "Brown", "Yellow", "Cyan", "Blue"])
planet_interesting_feature = pd.Series([
    "Closest planet to the Sun", 
    "Hottest planet in the solar system", 
    "Only planet known to support life", 
    "Has the tallest volcano (Olympus Mons)", 
    "Largest planet in the solar system", 
    "Has the most extensive ring system", 
    "Rotates on its side", 
    "Strongest winds in the solar system"
])
df = pd.DataFrame({
    "Name": planet_name,
    "Average Temperature (°C)": planet_average_temperature,
    "Radius (KM)": planet_radius,
    "Colour": planet_colour,
    "Interesting Feature": planet_interesting_feature
})
print(df)
originaldf = df

##############################################
# Adding columns using the dictionary method #
##############################################
# # adding a new column to the original dataframe to show who discovered each planet
# df["Discovered by"] = ["1","2","3","4","5","6","7","8"]
# print("\nAdding who discovered each planet")
# print(df)
# print()

# # adding a new column to the original dataframe to show the year it was discovered
# df["Discovered in"] = ["1","2","3","4","5","6","7","8"]
# print("\nAdding when the planet was discovered")
# print(df)
# print()

# # adding a new column to the original dataframe to show the elements of its composition
# df["Majorily composed of"] = ["1","2","3","4","5","6","7","8"]
# print("\nAdding what the planet is primarily composed of")
# print(df)
# print()

##############################################
# Adding columns using the concat method     #
##############################################
# adding a new column to the original dataframe to show who discovered each planet using the concat method
print("\nAdding who discovered each planet using the concat method")
new_discovered_by_column = pd.DataFrame({
    "Concat Discovered by": ["1","2","3","4","5","6","7","8"]
})

df2 = pd.concat([originaldf,new_discovered_by_column], axis=1)
print(df2)
print()

# adding a new column to the original dataframe to show the year it was discovered using the concat method
print("\nAdding when each planet was discovered using the concat method")
new_discovered_in_column = pd.DataFrame({
    "Concat Discovered in": ["1","2","3","4","5","6","7","8"]
})

df3 = pd.concat([df2,new_discovered_in_column], axis=1)
print(df3)
print()

# adding a new column to the original dataframe to show the elements of its composition using the concat method
print("\nAdding what each planet is primarily composed of using the concat method")
new_composition_data_column = pd.DataFrame({
    "Concat Composed of": ["1","2","3","4","5","6","7","8"]
})

df4 = pd.concat([df3,new_composition_data_column], axis=1)
print(df4)
print()

################################################################
# Adding columns using the concat method with combined data    #
################################################################
# adding a new column to the original dataframe to show who discovered each planet using the concat method
print("\nAdding who discovered each planet using the concat method")
new_discovered_by_column = pd.DataFrame({
    "Concat Discovered by": ["1","2","3","4","5","6","7","8"]
})

df2 = pd.concat([originaldf,new_discovered_by_column], axis=1)
print(df2)
print()



# pluto_data = pd.DataFrame({
#     "Name": ["a"],
#     "Average Temperature (°C)": [1],
#     "Radius (KM)": [1],
#     "Colour": ["a"],
#     "Interesting Feature": ["a"],
#     "Year Discovered": [1],
#     "Discovered By": ["a"],
#     "Composition": ["a"]
# })
# df = pd.concat([df, pluto_data], ignore_index=True)
# print(df)
 
