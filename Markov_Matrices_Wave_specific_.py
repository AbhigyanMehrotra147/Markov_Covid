import pandas as pd
from Super_class_for_normalization import Super_Normalization as SN
Wave_1_start = "2021-01-06"
Wave_1_end = "2021-06-06"
Wave_2_start = ""
Wave_2_end = ""
path_of_pickle_file = "C:/Users/Abhigyan/Desktop/Covid_Project_connected_to_github/Techniques of Markov Matrices/With Rolling Average/Technique-Wave specific matrices/Wave -1/Global Dynamic Mean Maximum/ Global Dynamic Mean Maximum new_cases.pickle"

Dataframe_wave_1 = pd.read_pickle(path_of_pickle_file)
print(Dataframe_wave_1)


def Get_matrix_of_wave(Dataframe):
    for country in Dataframe.columns:
        Stochastic_Matrix = SN.get_transition_matrix(
            dataframe=Dataframe, Country=country)
        print(Stochastic_Matrix)


Get_matrix_of_wave(Dataframe=Dataframe_wave_1)
