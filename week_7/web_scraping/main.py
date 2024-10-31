from bs4 import BeautifulSoup
import requests
import pandas as pd
############
# html_text = requests.get("https://www.scrapethissite.com/pages/simple/")
# # this returns all the properties, not just the webpage 
# print(dir(html_text))
############
# # this is the entire contents of the webpage
# print(html_text.text)
# we can also get this info like this
html_text = requests.get("https://www.scrapethissite.com/pages/simple/").text
#print(html_text)
############
souped_html = BeautifulSoup(html_text, 'lxml')
countries = souped_html.find_all('h3')
#print(countries)
# this returns a list of every country in the form
# <h3 class="country-name"><i class="flag-icon flag-icon-zw"></i>Zimbabwe</h3>
############
# for country in countries:
#     print(country.text)
############
# clean up the spaces
# for country in countries:
#     print(country.text.strip())
############
# import the data into a dataframe
# df = pd.DataFrame(country.text.strip() for country in countries)
# print(df)

# to get the other element values we need, we inspect the webpage and see they are stored as element classes
# we use class_ in order to differentiate it with the python keyword
country_capitals = souped_html.find_all('span', class_='country-capital')

for capital in country_capitals:
    print(capital.text.strip())

df = pd.DataFrame({
    "Country": [country.text.strip() for country in countries],
    "Capital": [capital.text.strip() for capital in country_capitals]
    })
print(df)