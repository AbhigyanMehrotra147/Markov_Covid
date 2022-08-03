import pandas as pd
import Super_class_for_normalization as SN

path_to_read_pickle = "C:/Users/Abhigyan/Desktop/Covid_Project_connected_to_github/Techniques of Markov Matrices/With Rolling Average/Technique_5 states/Global Dynamic Mean Maximum/new_cases.pickle"
DataFrame = pd.read_pickle(path_to_read_pickle)
# DataFrame.set_index('date', inplace=True)
Dictionary_of_Stochastic_Matrices = {}
for country in DataFrame:
    Dictionary_of_Stochastic_Matrices[country] = SN.Super_Normalization.get_transition_matrix(
        dataframe=DataFrame, Country=country, size=5)
for country_key in Dictionary_of_Stochastic_Matrices:
    print(country_key, end="\n")
    for row in Dictionary_of_Stochastic_Matrices[country_key]:
        print(row)
    print()
