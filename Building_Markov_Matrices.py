import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


class Markov_Matrices(object):
    path_to_read_pickle = "C:/Users/Abhigyan/Desktop/Markov Matrices(any number of states)/"

    # Function assigns state according to the value of the data point Value and Number of states asked for
    def assign_numeric_state(self, Dataframe, Data_point, No_of_states=10.0):
        if Data_point == np.nan or Data_point == 0.0:
            return -9999
        Country_Max = Dataframe.max()
        each_band_width = Country_Max / No_of_states
        i = 1
        band = each_band_width
        while band <= Country_Max:
            if Data_point <= band:
                return i-1
            i += 1
            band = each_band_width*i
        return -9999
    # Assigns more states to some areas than others

    def assign_custom_numeric_state(self, Dataframe, Data_point, No_of_states=10.0, divide_at=3):
        if Data_point == np.nan or Data_point == 0.0:
            return -9999
        Country_Max = Dataframe.max()
        each_band_width = Country_Max/No_of_states
        Double_state_bandwidth = each_band_width/2
        i = 0
        while i < divide_at*2:
            band = Double_state_bandwidth*i
            if Data_point < band:
                return i-1
            i += 1
        while i < No_of_states:
            band = each_band_width*i
            if Data_point < band:
                return i-1
            i += 1
        return -9999

    # Function converts the Normalized dataframe to any nuumber of steps
    # Steps are assigned numeric values

    def convert_to_number_of_states(self, No_of_states=10.0, catagory="new_cases", Normalization_Technique="GDM_"):
        Normalized_Dataframe = pd.read_pickle(
            Markov_Matrices.path_to_read_pickle + Normalization_Technique + catagory + ".pickle")
        for column in Normalized_Dataframe.columns:
            Normalized_Dataframe[column] = Normalized_Dataframe[column].apply(lambda x: self.assign_numeric_state(
                Dataframe=Normalized_Dataframe[column], Data_point=x, No_of_states=No_of_states))
        path_to_save_pickle = Markov_Matrices.path_to_read_pickle + \
            "States_Data_frame_" + Normalization_Technique + \
            str(round(No_of_states)) + "_" + catagory + ".pickle"
        Normalized_Dataframe.to_pickle(path_to_save_pickle)
        return path_to_save_pickle

    # Takes Average according to the number of days specified
    def take_average(self, Dataframe, Time_period=14):
        Averaged_Dataframe = pd.DataFrame()
        Rows = Dataframe.shape[0]
        for i in range(0, Rows-Time_period, Time_period):
            Averaged_Dataframe = Averaged_Dataframe.append(
                Dataframe.iloc[i:i+Time_period].mean(), ignore_index=True)
        return Averaged_Dataframe

    # Function assigns transition from state to state to the stochastic matrix
    def assign_transition(self, state_a, state_b, Stochastic_Matrix):
        if state_a < 0 or state_b < 0:
            return Stochastic_Matrix
        state_a = round(state_a)
        state_b = round(state_b)
        Stochastic_Matrix[state_a][state_b] += 1
        return Stochastic_Matrix
    # The fundtion generates Transition matrix according to the number of states
    # Generates the matrix for a country

    def Generate_Transition_Matrix(self, States_Series, No_of_states=10.0, step=10):

        Temp_Matrix = [[0]*round(No_of_states)]*round(No_of_states)
        Stochastic_Matrix = np.array(Temp_Matrix)
        No_of_rows = States_Series.shape[0]
        for i in range(0, No_of_rows-10, step):
            Stochastic_Matrix = self.assign_transition(
                States_Series.iloc[i], States_Series.iloc[i+step], Stochastic_Matrix=Stochastic_Matrix)
        sum_of_rows = np.sum(Stochastic_Matrix, 1)
        Stochastic_Matrix = Stochastic_Matrix.astype(np.float16)
        for m in range(round(No_of_states)):
            for n in range(round(No_of_states)):
                if sum_of_rows[m] == 0:
                    continue
                Stochastic_Matrix[m][n] = round(
                    Stochastic_Matrix[m][n] / sum_of_rows[m], 3)

        return Stochastic_Matrix


Mm = Markov_Matrices()
Path_to_read_pickle = Mm.convert_to_number_of_states(
    No_of_states=5.0, catagory="new_cases", Normalization_Technique="GDM_")
Dataframe = pd.read_pickle(Path_to_read_pickle)
# Dataframe = Mm.take_average(Dataframe=Dataframe, Time_period=14)
print(Dataframe)
for country in Dataframe.columns:
    print(country)
    Matrix = Mm.Generate_Transition_Matrix(
        Dataframe[country], No_of_states=5.0, step=1)
    print(Matrix)
    print()
