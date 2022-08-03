import sys
from Super_class_for_normalization import Super_Normalization as SN
import pandas as pd


path_to_read_pickle = "C:/Users/Abhigyan/Desktop/Covid_Project_connected_to_github/Techniques of Markov Matrices/With Rolling Average/Technique-Dynamic Time Frame Matrices/Global Dynamic Mean Maximum/"
Catagories = ["new_cases.pickle", "new_deaths.pickle"]
No_of_rows = None
Markov_Matrice_of_Frame = None
Time_Frame = 150
# variable holds the number of days we are incrementing by
step_of_time_frame = 10
# DataFrame of Matrices keys will be the date-durations
Dictionary_of_Matrices = {}
# path_to_save_text_files = "C: \Users\Abhigyan\Desktop\Covid_Project_connected_to_github\Techniques of Markov Matrices\With Rolling Average\Technique-Dynamic Time Frame Matrices\Global Dynamic Mean Maximum\New_Cases_text_files"
original_stdout = sys.stdout
Dataframe_with_states = pd.read_pickle(
    path_to_read_pickle + Catagories[0])
No_of_rows = Dataframe_with_states.shape[0]
for country in range(len(Dataframe_with_states.columns)):
    Nation = Dataframe_with_states.columns[country]

    Dictionary_of_Matrices[Nation] = {}
    for day in range(0, No_of_rows-Time_Frame, step_of_time_frame):
        Markov_Matrice_of_Frame = SN.get_transition_matrix(
            dataframe=Dataframe_with_states.iloc[day:day+Time_Frame], Country=Dataframe_with_states.columns[country])
        start_day = Dataframe_with_states.index[day]
        end_day = Dataframe_with_states.index[day+Time_Frame]
        Dictionary_of_Matrices[Nation][start_day +
                                       "-" + end_day] = Markov_Matrice_of_Frame

    with open(Nation + ".txt", 'w') as f:
        sys.stdout = f
        print(Nation)
        for key in Dictionary_of_Matrices[Nation]:
            print(key)
            print(Dictionary_of_Matrices[Nation][key])
            print()
        sys.stdout = original_stdout
