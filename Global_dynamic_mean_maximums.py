from Super_class_for_normalization import Super_Normalization as SN
import pandas as pd
import matplotlib.pyplot as plt


class Global_Dynamic_Mean(SN):
    # Initiailizing super class and this class
    # also assigning a catagory to each instant. Such as 'new_cases'
    def __init__(self, catagory):
        SN.__init__(self)
        self.catagory = catagory
        self.Dataframe_with_countries_as_column = SN.get_final_df_Dictionary(self)[
            self.catagory]

    # Functoin divides and adds each data points of frame by the global maximum
    # uses the applymap method which acts on each data point in the data set

    def Divide_by_max_and_add(self, frame_size):
        row_size = self.Dataframe_with_countries_as_column.shape[0]
        temp_data_frame = self.Dataframe_with_countries_as_column
        self.Dataframe_with_countries_as_column = self.Dataframe_with_countries_as_column.applymap(
            lambda x: 0)
        for i in range(1, row_size):
            if i > row_size-frame_size:
                global_dynamic_max = temp_data_frame.iloc[i:row_size].max(
                ).max()
                self.Dataframe_with_countries_as_column.iloc[i:row_size] += temp_data_frame[i:row_size].applymap(
                    lambda x: x/global_dynamic_max)
                continue
            global_dynamic_max = temp_data_frame.iloc[i:i
                                                      + frame_size+1].max(
            ).max()
            self.Dataframe_with_countries_as_column.iloc[i:i+frame_size +
                                                         1] = temp_data_frame.iloc[i:i+frame_size+1].applymap(lambda x: x/global_dynamic_max)

    # Function takes the mean of eachdata point acoording to the number of times vaules have been added to it
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
        self.Dataframe_with_countries_as_column.drop(
            self.Dataframe_with_countries_as_column.index[row_size-(frame_size+1):row_size], inplace=True)

        
    # Function plots the new cases from each country normalized to the global maximum
    def plot_data_frame(self, countries=None):
        super().plot_data_frame(
            self.Dataframe_with_countries_as_column, "Global Dynamic Mean", self.catagory, countries)


frame_size = 80
Catagory = ["new_cases", "new_deaths", "hosp_patients", "icu_patients"]
country = ["France", "Italy"]
Gdm = Global_Dynamic_Mean(Catagory[0])
Gdm.Divide_by_max_and_add(frame_size)
Gdm.Divide_by_frame_size(frame_size)
Gdm.plot_data_frame()
