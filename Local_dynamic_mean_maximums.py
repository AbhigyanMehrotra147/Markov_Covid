from numpy import column_stack
from Super_class_for_normalization import Super_Normalization as SN
import pandas as pd
import matplotlib.pyplot as plt


class Local_Dynamic_Mean_Maximum(SN):
    def __init__(self, catagory):
        SN.__init__(self)
        self.catagory = catagory
        self.Dataframe_with_countries_as_column = SN.get_final_df_Dictionary(self)[
            self.catagory]

    # Function divides and adds each data points of frame by the local maximum
    # uses the applymap method which acts on each data point in the data set
    def Divide_by_max_and_add(self, frame_size):
        temp_data_frame = self.Dataframe_with_countries_as_column
        row_size = temp_data_frame.shape[0]
        column_size = temp_data_frame.shape[1]

        # setting each element of the data frame with the value of 0
        self.Dataframe_with_countries_as_column = self.Dataframe_with_countries_as_column.applymap(
            lambda x: 0)

        for i in range(0, row_size):

            for j in range(0, column_size):

                # condition for the last frame
                if i > row_size-frame_size:
                    local_dynamic_max = temp_data_frame.iloc[i:row_size, j].max(
                    )
                    self.Dataframe_with_countries_as_column.iloc[i:row_size, j] += temp_data_frame.iloc[i:row_size, j].apply(
                        lambda x: x/local_dynamic_max)
                    continue

                # finding the local maximum within that frame
                local_dynamic_max = temp_data_frame.iloc[i:i +
                                                         frame_size + 1, j].max()

                # the apply function acts on each country's column's data point in the dataframe
                self.Dataframe_with_countries_as_column.iloc[i:i + frame_size + 1,
                                                             j] += temp_data_frame.iloc[i:i + frame_size + 1, j].apply(lambda x: x/local_dynamic_max)

        # print(self.Dataframe_with_countries_as_column)

    # Function takes the mean of each data point acoording to the number of times values have been added to it
    def Divide_by_frame_size(self, frame_size):
        row_size = self.Dataframe_with_countries_as_column.shape[0]
        count_foward = 1
        for i in range(0, row_size):

            # Condition for the data points within the first frame
            # ??????Shouldn't the first frame columns be also dropped
            if i < frame_size:
                # dividing all the countries for the same date with the frame size
                self.Dataframe_with_countries_as_column.iloc[
                    i] = self.Dataframe_with_countries_as_column.iloc[i]/count_foward
                count_foward += 1
                continue

            # Condition for the data points for the latter frames
            # dividing all the countries for the same date with the frame size
            self.Dataframe_with_countries_as_column.iloc[
                i] = self.Dataframe_with_countries_as_column.iloc[i]/frame_size

        # droping last frame columns
        self.Dataframe_with_countries_as_column.drop(
            self.Dataframe_with_countries_as_column.index[row_size-(frame_size+1):row_size], inplace=True)

        # print(self.Dataframe_with_countries_as_column)

    # Function plots the new cases from each country normalized to the local maximum

    def plot_data_frame(self, population_group, countries=None):
        super().plot_data_frame(self.Dataframe_with_countries_as_column,
                                "Local Dynamic Mean", self.catagory, countries, population_group)


frame_size = 120
Catagory = ["new_deaths", "hosp_patients", "icu_patients"]
for catagory in Catagory:
    i = 1
    for group in SN.population_in_ascending_order:
        Ldm = Local_Dynamic_Mean_Maximum(catagory)
        Ldm.Divide_by_max_and_add(frame_size)
        Ldm.Divide_by_frame_size(frame_size)
        Ldm.plot_data_frame(population_group="group" + str(i), countries=group)
        i += 1
