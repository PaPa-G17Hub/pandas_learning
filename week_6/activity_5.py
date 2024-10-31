# Plot the following data on a line graph using matplotlib:
# Research into more formatting options.
# Change the marker style and line colour of your plots.


# Activity = ["YouTube","Twitter","WhatsApp,","Raid:Shadow Legends","TikTok"]
# Monday = [2,1,3,0,3]
# Tuesday = [1,1,1,4,0]
# Wednesday = [3,0,0,2,1]
# Thursday = [6,0,2,3,0]
# Friday = [3,2,1,3,2]

days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
 
YouTube = [2,1,3,6,3]
Twitter = [1,1,0,0,2]
WhatsApp = [3,1,0,2,1]
Raid = [0,4,2,3,3]
TikTok = [3,0,1,0,2]

import matplotlib.pyplot as plt

# labelling the graph
plt.title("Screen Time")
plt.xlabel("Day")
plt.ylabel("Hours")

# plt.plot(days, YouTube, label="YouTube", linestyle="dashed")
# plt.plot(days, Twitter, label="Twitter", linestyle="dashed")
# plt.plot(days, WhatsApp, label="WhatsApp", linestyle="dashdot")
# plt.plot(days, Raid, label="Raid: Shadow Legends", linestyle="dotted")
# plt.plot(days, TikTok, label="TikTok", linestyle="solid")

# Displaying the data better to show ranking
plt.ylim(bottom = 0, top = 7)

plt.plot(days, YouTube, label="YouTube", marker="$x$")
plt.plot(days, Twitter, label="Twitter", marker="$o$")
plt.plot(days, WhatsApp, label="WhatsApp", marker="$+$")
plt.plot(days, Raid, label="Raid: Shadow Legends", marker="$>$")
plt.plot(days, TikTok, label="TikTok", marker="$@$")

plt.legend()
plt.show()



# Playing with marker styles
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html
######################################
# Unfilled markers
######################################
from matplotlib.lines import Line2D
from matplotlib.markers import MarkerStyle
from matplotlib.transforms import Affine2D

text_style = dict(  horizontalalignment='right',
                    verticalalignment='center',
                    fontsize=12,
                    fontfamily='monospace')
marker_style = dict(linestyle=':',
                    color='0.8',
                    markersize=10,
                    markerfacecolor="tab:blue",
                    markeredgecolor="tab:blue")

def format_axes(ax):
    ax.margins(0.2)
    ax.set_axis_off()
    ax.invert_yaxis()

def split_list(a_list):
    i_half = len(a_list) // 2
    return a_list[:i_half], a_list[i_half:]

######################################
# Filled markers
######################################
######################################
# Markers created from TeX symbols
######################################
######################################
# Markers created from Paths
######################################
