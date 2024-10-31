# Remember your data from results.csv?
import pandas as pd
####################################################################################################################
# The dataset might shorten itself to fit nicely on the screen.
# If you want to see all rows without any truncation, we can turn off this default behaviour with the following:
#
#pd.set_option('display.max_rows', None)
####################################################################################################################

####################################################################################################################
# Reads the csv file into a panda dataframe
#
results_df = pd.read_csv("results.csv")
####################################################################################################################
## Display all results
#
# print(results_df)
####################################################################################################################
## Displays the dataframes column headers
#
#print(results_df.columns)
####################################################################################################################
# How many different kinds of tournaments were played?
#
# print("How many different kinds of tournaments were played?")
# distinct_tournaments_df = results_df.value_counts("tournament")
# print(len(distinct_tournaments_df.index))
####################################################################################################################
# # How many matches were played under each tournament?
#
# print("How many matches were played under each tournament?")
# print(distinct_tournaments_df)
####################################################################################################################
# # The most reported home team and away team
#
print("The most reported home team and away team")
home_team_df = results_df.value_counts("home_team")
print(home_team_df[ ])
print(home_team_df.min())

# print(home_team_df[0])
# # The least reported home team and away team
# print("The least reported home team and away team")
