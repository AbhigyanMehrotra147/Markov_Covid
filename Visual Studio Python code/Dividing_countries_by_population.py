import pandas as pd
# Pasting the name the csv file containg information of population and population density
Csv_population = 'Population_and_population_density.csv'
Pop_data_frame = pd.read_csv(Csv_population)
Pop_data_frame.rename()
Pop_data_frame.set_index('name')
