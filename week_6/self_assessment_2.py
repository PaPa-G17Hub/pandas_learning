import pandas as pd

df = pd.read_csv('results.csv')

#------------------------------------------------------
#                      Task 1                          |
# How many different kinds of tournaments were played? |
#------------------------------------------------------

print(df['tournament'].nunique())

#------------------------------------------------------
#                      Task 2                          |
# How many matches were played under each tournament?  |
#------------------------------------------------------

print(df['tournament'].value_counts())

#------------------------------------------------------
#                      Task 3                          |
#      The most reported home team and away team?      |
#------------------------------------------------------
print(df['home_team'].value_counts())
print(df['away_team'].value_counts())

'or'

print(df['home_team'].mode())
print(df['away_team'].mode())

#------------------------------------------------------
#                      Task 4                          |
#       The least reported home team and away team?    |
#------------------------------------------------------

home_team_value_counts = df['home_team'].value_counts()
print(home_team_value_counts[home_team_value_counts == 1])

# (N.B - query won’t quite work on this unless you convert the value count series to a frame)



#--------------------------------------------------------
#                      Task 5                            |
#        How many times England played at home in        | 
#                   each tournament                      |
#--------------------------------------------------------

print(df.query('home_team=="England"').groupby('tournament')['home_team'].count())

#--------------------------------------------------------
#                      Task 6                            |
# How many times England scored more than the “average”  | 
#              amount of goals at a home match.          |
#--------------------------------------------------------

'For better context, find out how many matches are recorded for England overall. It puts the 325 matches into much better context!'

mean_home_score = df['home_score'].mean()
print(mean_home_score)

print(len(df.query("home_team=='England' and home_score>@mean_home_score")))

print(df.query('home_team=="England"').shape[0])

#--------------------------------------------------------
#                      Task 7                            |
# How many times England scored more than the “average”  | 
#              amount of goals at an away match.         |
#--------------------------------------------------------

mean_away_score = df['away_score'].mean()
print(mean_away_score)

print(len(df.query("home_team=='England' and away_score>@mean_away_score")))

print(df.query('home_team=="England"').shape[0])

#--------------------------------------------------------
#                      Task 8                            |
#         What is England’s average amount of            |
#                goals scored at home?                   |
#--------------------------------------------------------

# queries the dataframe to onlresults where England is the home team, and then finds the mean of the home_score column

england_mean = df.query("home_team=='England'")['home_score'].mean()
print(england_mean)


#--------------------------------------------------------
#                      Task 9                            |
#        What is each team's average amount of           |
#             goals scored at home and away?             |
#--------------------------------------------------------

# queries the dataframe to onlresults where England is the home team, and then finds the mean of the home_score column

print(df.groupby('home_team')['home_score'].mean().sort_values(ascending=False))
