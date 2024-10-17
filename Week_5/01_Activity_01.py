# Create a dataframe to store information on the planets of the solar system.

# For each planet, record:
#     • its name
#     • the average temperature
#     • the planet’s radius in KM
#     • the planet’s colour
#     • an interesting feature of the planet.
import pandas as pd
import numpy as np

planet_name = pd.Series(["Mecury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"])
planet_average_temperature = pd.Series([167,464,15,-65,-110,-140,-195,-200,-225])
planet_diameter = pd.Series([4879,12104,12756,6792,142,984,120,536,51,118,49,528,2376])
planet_radius = pd.Series([2440, 6052, 6378, 6051.8, 3389.5, 69911, 58232, 25362, 24622])
planet_colour = pd.Series(["Green", "Gray", "Yellow", "Butterscotch", "Orange", "Brown", "Pale Green", "Pale Blue", "Red"])
planet_interesting_feature = pd.Series(["No", "No", "No", "No", "Yes", "Yes", "Yes", "Yes", "No"])

df = pd.DataFrame({
    "Planet Name": planet_name, 
    "Average Temperature": planet_average_temperature,
    "Radius KM": planet_radius,
    "Colour": planet_colour,
    "Interesting Feature": planet_interesting_feature
    })

print(df)