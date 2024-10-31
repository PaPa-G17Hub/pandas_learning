# We turned an Excel file into a dataframe using .read_excel()
# Research into turning a dataframe into an Excel file and turn your planets frame into a spreadsheet.
import pandas as pd
import numpy as np
import openpyxl as openpyxl 

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

# Create a workbook
from openpyxl import Workbook
planet_workbook = Workbook()

# A workbook is always created with at least one worksheet. You can get it by using the Workbook.active property:
planet_worksheet = planet_workbook.active

# Sheets are given a name automatically when they are created. They are numbered in sequence (Sheet, Sheet1, Sheet2, …). You can change this name at any time with the Worksheet.title property:
planet_worksheet.title = "Planet Information"

#