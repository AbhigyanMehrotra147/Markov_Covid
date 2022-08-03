import pandas as pd
from Super_class_for_normalization import Super_Normalization
path_to_read_pickle = "C:/Users/Abhigyan/Desktop/Covid_Project_connected_to_github/Techniques of Markov Matrices/With Rolling Average/Technique-Averaging states in a time period/Time-Period  = 7 days/Global Dynamic Mean Maximum/New Cases/new_cases.pickle"
States_dataframe = pd.read_pickle(path_to_read_pickle)
# States_dataframe.to_excel("test.xlsx")
# print(States_dataframe)
# exit()
for country in States_dataframe.columns:
    print(country)
    print(Super_Normalization.get_transition_matrix(
        dataframe=States_dataframe, Country=country))
