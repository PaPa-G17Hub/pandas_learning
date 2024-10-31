# Data used within the matplot lib session
# Can be distributed in the session to save anyone having to type out reems of data
import pandas as pd
import matplotlib.pyplot as plt
# -----------------------------------------------------------------------------------
#                                  Bar Chart Data
# -----------------------------------------------------------------------------------

# df = pd.DataFrame({
#     "Locations" : [
#     "Twitter",
#     "Facebook",
#     "LinkedIn",
#     "Indeed",
#     "Instagram"
# ],
#     "Responses" : [3,11,16,13,2],
# })

# plt.title("Standard Bar chart")
# plt.bar("Locations","Responses", data=df)
# plt.xlabel("Advert Location")
# plt.ylabel("Application Recevied")
# plt.show()

# plt.title("Horizontal Bar chart")
# plt.barh("Locations","Responses", data=df)
# plt.xlabel("Advert Location")
# plt.ylabel("Application Recevied")
# plt.show()

# plt.title("Sorted Standard Bar chart")
# df = df.sort_values("Responses")
# plt.bar("Locations","Responses", data=df)
# plt.xlabel("Advert Location")
# plt.ylabel("Application Recevied")
# plt.show()

# plt.title("Sorted Coloured Standard Bar chart")
# df = df.sort_values("Responses")
# bar_colours = ["red" if x == df["Responses"].max() else "blue" for x in df["Responses"]]
# plt.bar("Locations","Responses", data=df, color = bar_colours)
# plt.xlabel("Advert Location")
# plt.ylabel("Application Recevied")
# plt.show()

# -----------------------------------------------------------------------------------
#                                  Stacked Bar Chart Data
# -----------------------------------------------------------------------------------

# df = pd.DataFrame({
#     "Engineering":[56,13,1],
#     "Computer Science":[77,23,4],
#     "English Lit":[35,48,9],
#     "Economics": [65,45,19]
# }, index=["Male", "Female", "Non-Binary"])

# my_plot = df.plot.barh(stacked=True)
# plt.show()

# # Transposing the data frame
# df=df.T
# my_plot = df.plot.barh(stacked=True)
# plt.show()

# # changing the colour theme
# # https://matplotlib.org/stable/users/explain/colors/colormaps.html
# df=df.T
# my_plot = df.plot.barh(stacked=True, colormap="summer")
# plt.show()

# -----------------------------------------------------------------------------------
#                                  Pie Chart Data
# -----------------------------------------------------------------------------------

# roles = [    
#     "Front-end", 
#     "Back-end",
#     "Full-stack",
#     "DevOps"
#     ]

# employees = [52,36,28,11]
# plt.title("Standard pie chart")
# plt.pie(employees, labels=roles)
# plt.show()

# plt.title("Displaying the percentage")
# plt.pie(employees, labels=roles,autopct="%.1f%%")
# plt.show()

# plt.title("Displaying an exploded segment")
# plt.pie(employees, labels=roles,autopct="%.1f%%", explode=[0.2,0,0,0])
# plt.show()

# plt.title("Displaying a different colour map")
# plt.pie(employees, labels=roles,autopct="%.1f%%", explode=[0.2,0,0,0], colormap="Purples")
# plt.show()
# # not working yet

# -----------------------------------------------------------------------------------
#                                  Scatter
# -----------------------------------------------------------------------------------

# number_of_placements=list(range(1,11))
# responses_received = [14, 21, 34, 36, 45, 51, 54, 63, 78, 92]
# plt.scatter(number_of_placements, responses_received)
# plt.title("Job Posting Junior Dev Role")
# plt.xlabel("Number of Place Advertised")
# plt.ylabel("Responses Recvived")
# plt.show()

# # need to convert the data into an numpy array in order to make a line of best fit
# import numpy as np
# number_of_placements=np.array(range(1,11))
# responses_received=np.array([14, 21, 34, 36, 45, 51, 54, 63, 78, 92])
# a,b = np.polyfit(number_of_placements,responses_received,1)
# plt.plot(number_of_placements, a*number_of_placements+b)
# plt.scatter(number_of_placements, responses_received)
# plt.title("Using a line of best fit")
# plt.xlabel("Number of Place Advertised")
# plt.ylabel("Responses Recvived")
# plt.show()

# -----------------------------------------------------------------------------------
#                             Box Plots and Histogram Data
# -----------------------------------------------------------------------------------

dev_ages=[
        45, 23, 57, 27, 37, 39, 61, 48, 23, 27, 
        59, 60, 28, 41, 25, 39, 22, 46, 48, 52, 
        38, 41, 52, 30, 46, 62, 25, 34, 52, 35, 
        48, 43, 21, 40, 22, 22, 57, 25, 21, 30, 
        55, 50, 54, 30, 43, 40, 53, 46, 36, 61, 
        35, 39, 40, 31, 29, 65, 28, 57, 39, 36, 
        20, 49, 42, 29, 62, 52, 29, 57, 39, 32
        ]

# plt.boxplot(dev_ages,vert=0)
# plt.title("Box plot showing Developer Ages at Code Nation")
# plt.xlabel("Age")
# plt.show()

# plt.hist(dev_ages)
# plt.title("Histogram showing Developer Ages at Code Nation")
# plt.xlabel("Developer Ages")
# plt.ylabel("Frequency")
# plt.show()

# plt.hist(dev_ages, edgecolor="black")
# plt.title("Histogram with clearer splits")
# plt.xlabel("Developer Ages")
# plt.ylabel("Frequency")
# plt.show()

# plt.hist(dev_ages, edgecolor="black",
#          bins=[20,25,30,35,40,45,50,55,60,65])
# plt.title("Histogram with clearer splits and bars split into 5's")
# plt.xlabel("Developer Ages")
# plt.ylabel("Frequency")
# plt.show()

# -----------------------------------------------------------------------------------
#                             Saving plots
# -----------------------------------------------------------------------------------
plt.hist(dev_ages, edgecolor="black",
         bins=[20,25,30,35,40,45,50,55,60,65])
plt.title("Saving our plots")
plt.xlabel("Developer Ages")
plt.ylabel("Frequency")
# call savefig before plt.show()
plt.savefig("dev_age_plot.png")
plt.show()