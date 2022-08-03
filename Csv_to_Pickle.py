import pandas as pd
url = url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
Csv_dataframe = pd.read_csv(url)
Csv_dataframe.to_pickle("pickled_data.pickle")
print(Csv_dataframe)
