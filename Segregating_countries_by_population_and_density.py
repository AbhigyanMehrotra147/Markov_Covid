import pandas as pd
# Pasting the name the csv file containg information of population and population density
Csv_population = 'Population_and_population_density.csv'
Pop_data_frame = pd.read_csv(Csv_population)
Pop_data_frame.rename(columns={'name': 'country'}, inplace=True)
Pop_data_frame.set_index('country', inplace=True)
# Only_pop is the dataframe containing only population values and not pipulation density values
Only_pop = Pop_data_frame['pop']
Only_pop = Only_pop.sort_values()
smallest_populations = Only_pop.iloc[0:12].index
second_smallest_populations = Only_pop.iloc[12:24].index
second_largest_populations = Only_pop.iloc[24:36].index
largest_populations = Only_pop.iloc[36:49].index
# print(smallest_populations)
Population_in_order = [smallest_populations, second_smallest_populations,
                       second_largest_populations, largest_populations]
Only_density = Pop_data_frame['popDensity']
Only_density.sort_values()
smallest_density = Only_density.iloc[0:12]
second_smallest_density = Only_density.iloc[12:24]
second_largest_density = Only_density.iloc[24:36]
largest_density = Only_density.iloc[36:49]
Density_in_order = [smallest_density, second_smallest_density,
                    second_largest_density, largest_density]
# print(Population_in_order)
