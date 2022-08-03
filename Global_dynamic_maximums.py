
from Super_class_for_normalization import Super_Normalization as SN
import pandas as pd
import matplotlib.pyplot as plt


class Global_Dynamic(SN):
    # Initiailizing super class and this class
    # also assigning a catagory to each instant. Such as 'new_cases'
    def __init__(self):
        SN.__init__(self)
        self.Dataframe_with_countries_as_column = pd.DataFrame()
        self.Dataframe_dictionary = SN.get_final_df_Dictionary(self)
        self.max_array = [0]*self.data_frame.shape[0]

    # Creates the maximum array
    # The maximum array holds :

    def Create_max_array(self, catagory="new_cases", frame_size=90):
        # Creating deep copy so that changes do not reflect in the origninal dataframe
        # Assigning cataogry to Dataframe_with_countries_as_column
        self.Dataframe_with_countries_as_column = self.Dataframe_dictionary[catagory].copy(
            deep=True)
        row_size = self.Dataframe_with_countries_as_column.shape[0]
        for i in range(0, row_size):
            if i > row_size - frame_size:
                global_frame_max = self.Dataframe_with_countries_as_column.iloc[i:row_size].max(
                ).max()
                for j in range(i, row_size):
                    if self.max_array[j] < global_frame_max:
                        self.max_array[j] = global_frame_max
                continue
            global_frame_max = self.Dataframe_with_countries_as_column.iloc[i: i + frame_size+1].max(
            ).max()
            for j in range(i, i + frame_size+1):
                if self.max_array[j] < global_frame_max:
                    self.max_array[j] = global_frame_max

    # Functoin divides each data point by the global maximum
    # uses the applymap method which acts on each data point in the data set

    def Divide_by_max_array(self):
        row_size = self.Dataframe_with_countries_as_column.shape[0]
        for i in range(0, row_size):
            self.Dataframe_with_countries_as_column.iloc[
                i] = self.Dataframe_with_countries_as_column.iloc[i]/self.max_array[i]

    # Function plots the new cases from specified country normalized to the global maximum
    def plot_data_frame(self, path_to_save="", Countries=None, name_on_saving=""):
        super().plot_data_frame(
            DathFrame_to_be_plotted=self.Dataframe_with_countries_as_column, countries=Countries, path_to_save=path_to_save, name_on_saving=name_on_saving)


Catagories = ["new_cases", "new_deaths"]
Gd = Global_Dynamic()
# path_to_save_dataframe = "C:/Users/Abhigyan/Desktop/Covid_Project_connected_to_github/Techniques of Markov Matrices/With Rolling Average/Technique-Averaging states in a time period/Time-Period  = 14 days/Global Dynamic Maximum/"
path_to_save_dataframe = "C:/Users/Abhigyan/Desktop/Covid_Project_connected_to_github/Techniques of Markov Matrices/With Rolling Average/Technique-Dynamic Time Frame Matrices/Global Dynamic Maximum/"
# Change_in_path = ["New Cases/", "New Deaths/"]
i = 0
for cat in Catagories:
    Gd.Create_max_array(catagory=cat, frame_size=90)
    Gd.Divide_by_max_array()
    SN.save_and_convert_to_three_state_with_country_specific_max(
        dataframe=Gd.Dataframe_with_countries_as_column, file_name=path_to_save_dataframe+cat, time_period=None)
    i += 1
