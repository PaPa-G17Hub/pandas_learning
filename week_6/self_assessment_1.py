import pandas as pd

planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planet_temp = ["167C", "464C", "15C", "65C", "-110C", "-140C", "-195C", "-200C"]
planet_size = ["2440km", "6052km", "6371km", "3390km", "69911km", "58232km", "25362km", "24622km"]
planet_colour = ["Grey", "White", "Blue", "Red", "Beige", "Beige", "Blue", "Blue"]
planet_feature = ["Smallest Planet", "Hottest Planet", "Supports Life!", "Iron Soil", "Giant Storm", "Rings", "Extreme Seasons", "Icy"]

df = pd.DataFrame({
    "Planet Name": planet_names,
    "Average Temp": planet_temp,
    "Radius": planet_size,
    "Colour": planet_colour,
    "Notable Feature": planet_feature
})
print("\nFrom Self Assessment")
print(df)

my_planet_name = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
my_planet_average_temperature = [167, 464, 15, -65, -110, -140, -195, -200]
my_planet_radius = [2439.7, 6051.8, 6371, 3389.5, 69911, 58232, 25362, 24622]
my_planet_colour = ["Grey", "Yellow", "Blue", "Red", "Brown", "Yellow", "Cyan", "Blue"]
my_planet_interesting_feature = [
    "Closest planet to the Sun", 
    "Hottest planet in the solar system", 
    "Only planet known to support life", 
    "Has the tallest volcano (Olympus Mons)", 
    "Largest planet in the solar system", 
    "Has the most extensive ring system", 
    "Rotates on its side", 
    "Strongest winds in the solar system"
]

my_df = pd.DataFrame({
    "Name": my_planet_name,
    "Average Temperature (°C)": my_planet_average_temperature,
    "Radius (KM)": my_planet_radius,
    "Colour": my_planet_colour,
    "Interesting Feature": my_planet_interesting_feature
})
print("\nFrom my work & self assessment")
print(my_df)

print("\nSaving to an excel file")
# my_df.to_excel("planets.xlsx", index=False)

# Amend your solar system dataframe to add: 
# • Who discovered each planet 
# • The year it was discovered 
# • Elements of its composition

discoverer = ["not known", "not known", "not known", "not known", "not known", "not known", "William Herschel", "Johann Galle"]
year_discovered = ["not known", "not known", "not known", "not known", "not known", "not known", "1781", "1846"]
composition = [ "Oxygen, Sodium", "Carbon Dioxide, Nitrogen", "Nitrogen, Oxygen", "Carbon Dioxide, Nitrogen", "Hydrogen, Helium", "Hydrogen, Helium", "Hydrogen, Helium", "Hydrogen, Helium" ]
