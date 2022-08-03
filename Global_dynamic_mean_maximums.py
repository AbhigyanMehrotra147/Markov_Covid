import numpy as np
from Super_class_for_normalization import Super_Normalization as SN
import pandas as pd
import matplotlib.pyplot as plt


class Global_Dynamic_Mean(SN):
    # Initiailizing super class and this class
    # also assigning a catagory to each instant. Such as 'new_cases'
    def __init__(self):
        SN.__init__(self)
        self.Dataframe_dictionary = SN.get_final_df_Dictionary(self)
        self.Dataframe_with_countries_as_column = pd.DataFrame()

    # Functoin divides and adds each data points of frame by the global maximum
    # uses the applymap method which acts on each data point in the data set

    def Divide_by_max_and_add(self, frame_size=120, catagory="new_cases"):
        # Creating a deep copy because we dont want the changes to reflect in the original data frame
        # Assigning cataogry to Dataframe_with_countries_as_column
        self.Dataframe_with_countries_as_column = self.Dataframe_dictionary[catagory].copy(
            deep=True)
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
                                                         1] += temp_data_frame.iloc[i:i+frame_size+1].applymap(lambda x: x/global_dynamic_max)

    # Function takes the mean of eachdata point acoording to the number of times vaules have been added to it
    def Divide_by_frame_size(self, frame_size=120):
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
    def plot_data_frame(self, path_to_save="", Countries=[], name_on_saving=""):
        SN.plot_data_frame(
            DathFrame_to_be_plotted=self.Dataframe_with_countries_as_column, countries=Countries, path_to_save=path_to_save, name_on_saving=name_on_saving)


def rolling_average(new_df, rolling_days):
    row_count = new_df.shape[0]
    column_count = new_df.shape[1]

    temp_data_frame = new_df.copy()

    for country_index in range(column_count):

        index_counter = 0

        # for each date in each country
        for date_index in range(row_count):

            # surpass all the Nan values in the dataframe then only proceeding
            if not (np.isnan(new_df.iloc[date_index, country_index])):

                # summing of the rolling days from the copied data frame
                # assuming that the dataframe is larger than the rolling_days parameter
                rolling_counter_index = date_index
                ending_rolling_counter_index = date_index + rolling_days

                # finding the mean of all the days within the rolling days window
                rolling_days_mean = temp_data_frame.iloc[rolling_counter_index:
                                                         ending_rolling_counter_index, country_index].mean()

                # updating the new value in the original dataframe
                # doing -1 to put the value into the last element of rolling day window (if rolling_days = 7 then into the 7th element i.e (6th index not 7th index)
                new_df.iloc[ending_rolling_counter_index -
                            1, country_index] = rolling_days_mean

                # reached the end of the dataframe
                if(ending_rolling_counter_index - 1 == row_count-1):
                    break

                # this function will work for the first number of rolling days
                # except the last day where we are actually filling the new average value
                if index_counter < rolling_days - 1:
                    # removing (here filling with Nan value) the first rolling days values from the dataframe
                    new_df.iloc[date_index, country_index] = np.nan
                    index_counter += 1
    return new_df


frame_size = 120
Gdm = Global_Dynamic_Mean()
Catagories = ["new_cases", "new_deaths"]
path_to_save_pickle_file = "C:/Users/Abhigyan/Desktop/First_Derivative_Rolling_Average_28_days/Second_Derivative/Rolling_Average/"
path_to_save_plots = "C:/Users/Abhigyan/Desktop/Plots_GDM/plots_of_individual_countries_new_cases/"
for cat in Catagories:
    Gdm.Divide_by_max_and_add(frame_size=frame_size, catagory=cat)
    Gdm.Divide_by_frame_size(frame_size=frame_size)
    Gdm.Dataframe_with_countries_as_column = SN.Get_Differentiaion(
        Gdm.Dataframe_with_countries_as_column)
    Gdm.Dataframe_with_countries_as_column = rolling_average(
        new_df=Gdm.Dataframe_with_countries_as_column, rolling_days=28)
    Gdm.Dataframe_with_countries_as_column = SN.Get_Differentiaion(
        Gdm.Dataframe_with_countries_as_column)
    Gdm.Dataframe_with_countries_as_column = rolling_average(
        new_df=Gdm.Dataframe_with_countries_as_column, rolling_days=28)
    Gdm.Dataframe_with_countries_as_column.to_pickle(
        path_to_save_pickle_file + "GDM_" + cat + ".pickle")
