from tkinter import ON
# File is the code for getting standard and unique colors for all the countries
import pandas as pd
import secrets
url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
DataFrame = pd.read_csv(url)
filt = DataFrame.continent == "Europe"
DataFrame = DataFrame[filt]
Only_European_countries = DataFrame.location.value_counts()
No_of_european_countries = Only_European_countries.shape[0]
countries_as_a_list = Only_European_countries.index
COLOR = {}
for country in countries_as_a_list:
    COLOR[country] = '#' + secrets.token_hex(3)
print(COLOR)
