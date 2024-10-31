# install matplotlib
# pip install matplotlib
import matplotlib.pyplot as plt

# Types of graphs possible
# Line Graph - displays changes over time
# Bar Chart - compares different categories of data
# Stacked Bar Chart - shows how the pieces of data make up the whole
# Pie Chart - quickly and clearly show how the parts of data make up a whole result.
# Scatter Graph
# Box Plots
# Histogram 

years = [2018,2019,2020,2021,2022,2023]
python_postion = [7,4,4,3,4,3]

# plt.plot(years, python_postion)
# plt.show()

# Improving the presenation with labelling
plt.title("Most popular programming language")
plt.xlabel("Year")
plt.ylabel("Position")
# plt.plot(years, python_postion)
# plt.show()

# Displaying the data better to show ranking
plt.ylim(bottom = 14, top = 0)
# plt.plot(years, python_postion)
# plt.show()

# adding a new language
js_position = [1,1,1,1,1,1]
sql_position = [4,3,3,4,3,4]
typescript_position = [12,10,9,7,5,5]
plt.plot(years, python_postion)
plt.plot(years, js_position)
plt.plot(years, sql_position)
plt.plot(years, typescript_position)

# adding a grouped graph legend
# plt.legend([
#     "Python",
#     "JavaScript",
#     "SQL",
#     "TypeScript"
# ])

# adding a label using the plot method 
# plt.plot(years, python_postion, label = "Python")
# plt.plot(years, js_position, label = "JavaScript")
# plt.plot(years, sql_position, label = "SQL")
# plt.plot(years, typescript_position, label = "Typescript")
# can use plt.legend without an argument now
#plt.legend()

# format the graph using linestyle to help with readability
# linestyle options are:
# 'solid'
# 'dotted'
# 'dashed'
# 'dashdot'
# 'loosely dotted'
# 'dotted'
# 'densely dotted'
# 'long dash with offset'
# 'loosely dashed'
# 'dashed'
# 'densely dashed'
# 'loosely dashdotted'
# 'dashdotted'
# 'densely dashdotted'
# 'dashdotdotted'
# 'loosely dashdotdotted'
# 'densely dashdotdotted'

plt.plot(years, python_postion, label = "Python") # linestyle defaults to a solid line
plt.plot(years, js_position, label = "JavaScript", linestyle="dashed")
plt.plot(years, sql_position, label = "SQL", linestyle="dotted")
plt.plot(years, typescript_position, label = "Typescript", linestyle="dashdot")

# can use plt.legend without an argument now
plt.legend()
plt.show()