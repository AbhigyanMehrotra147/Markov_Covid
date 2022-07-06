from numpy import column_stack
from Super_class_for_normalization import Super_Normalization as SN
import pandas as pd
import matplotlib.pyplot as plt


class Local_Dynamic_Mean_Maximum(SN):
    # Initiializing super class and this class
    # Also assiging a catagory such as 'new_cases'
    def __init__(self, catagory):
        SN.__init__(self)
        self.catagory = catagory
        self.Dataframe_with_countries_as_column = SN.get_final_df_Dictionary(self)[
            self.catagory]

    # Functoin divides and adds each data points of frame by the local maximum
    # uses the apply method which acts on each data point in the a series

    def Divide_by_max_and_add(self, frame_size):
        row_size = self.Dataframe_with_countries_as_column.shape[0]
        column_size = self.Dataframe_with_countries_as_column.shape[1]
        temp_data_frame = self.Dataframe_with_countries_as_column
        self.Dataframe_with_countries_as_column = self.Dataframe_with_countries_as_column.applymap(
            lambda x: 0)
        for i in range(0, row_size):
            for j in range(0, column_size):
                if i > row_size-frame_size:
                    local_dynamic_max = temp_data_frame.iloc[i:row_size, j].max(
                    )
                    self.Dataframe_with_countries_as_column.iloc[i:row_size, j] += temp_data_frame.iloc[i:row_size, j].apply(
                        lambda x: x/local_dynamic_max)
                    continue
                local_dynamic_max = temp_data_frame.iloc[i:i +
                                                         frame_size+1, j].max()
                self.Dataframe_with_countries_as_column.iloc[i:i+frame_size +
                                                             1, j] += temp_data_frame.iloc[i:i+frame_size+1, j].apply(lambda x: x/local_dynamic_max)

    # Function takes the mean of each data point and divides acoording to the number of times vaules have been added to it
    def Divide_by_frame_size(self, frame_size):
        row_size = self.Dataframe_with_countries_as_column.shape[0]
        count_foward = 1
        for i in range(0, row_size):
            if i < frame_size:
                self.Dataframe_with_countries_as_column.iloc[
                    i] = self.Dataframe_with_countries_as_column.iloc[i]/count_foward
                count_foward += 1
                continue
            self.Dataframe_with_countries_as_column.iloc[
                i] = self.Dataframe_with_countries_as_column.iloc[i]/frame_size
        # Dropping columns which are only divided by a maximum very close in their vicinity
        self.Dataframe_with_countries_as_column.drop(
            self.Dataframe_with_countries_as_column.index[row_size-(frame_size+1):row_size], inplace=True)

    # Function to be made much better in futrue
    # Function plots the new cases from specified country normalized to the local maximum

    def plot_data_frame(self, countries=None):
        super().plot_data_frame(
            self.Dataframe_with_countries_as_column, "Local Dynamic Mean", self.catagory, countries)


frame_size = 80
Catagory = ["new_cases", "new_deaths", "hosp_patients", "icu_patients"]
country = ["Germany", "France", "Italy"]
Ldm = Local_Dynamic_Mean_Maximum(Catagory[1])
Ldm.Divide_by_max_and_add(frame_size)
Ldm.Divide_by_frame_size(frame_size)
Ldm.plot_data_frame()
