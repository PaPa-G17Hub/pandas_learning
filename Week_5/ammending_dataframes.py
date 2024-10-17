import pandas as pd
import numpy as np

languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])
positions = pd.Series([3,1,2,4])

# Using a dictionary, with a key, value pair, to manually build a new dataframe
df3 = pd.DataFrame({
    "Languages": languages,
    "Ranking": positions

})

print()
print(df3)
# print()

