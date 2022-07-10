from Super_class_for_normalization import Super_Normalization as SN
import pandas as pd
import matplotlib.pyplot as plt


class Global_Dynamic(SN):
    # Initiailizing super class and this class
    # also assigning a catagory to each instant. Such as 'new_cases'
    def __init__(self, catagory):
        SN.__init__(self)
        self.catagory = catagory
        self.Dataframe_with_countries_as_column = SN.get_final_df_Dictionary(self)[
            self.catagory]
        self.max_array = [0]*self.data_frame.shape[0]

    # Creates the maximum array
    # The maximum array holds :

    def Create_max_array(self, frame_size):
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
    def plot_data_frame(self, countries=None):
        super().plot_data_frame(
            self.Dataframe_with_countries_as_column, "Global Dynamic", self.catagory, countries)


Catagory = ["new_cases", "new_deaths", "hosp_patients", "icu_patients"]
country = ["France", "Germany", "Italy"]
Gd = Global_Dynamic(Catagory[0])
Gd.Create_max_array(60)
Gd.Divide_by_max_array()
Gd.plot_data_frame()
