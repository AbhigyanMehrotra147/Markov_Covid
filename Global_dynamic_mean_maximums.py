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

    def Divide_by_max_and_add(self, frame_size, catagory):
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
                                                         1] = temp_data_frame.iloc[i:i+frame_size+1].applymap(lambda x: x/global_dynamic_max)

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
    def plot_data_frame(self, Population_group, Catagory="new_cases", Countries=None,):
        super().plot_data_frame(
            Df=self.Dataframe_with_countries_as_column, Type="Global Dynamic Mean", catagory=Catagory, countries=Countries, population_group=Population_group)

    # def plot_data_frame(self, countries=None):
    #     super().plot_data_frame(
    #         self.Dataframe_with_countries_as_column, "Global Dynamic Mean", self.catagory, countries)


frame_size = 90
Catagory = ["new_cases", "new_deaths", "hosp_patients", "icu_patients"]
country = ["France", "Italy"]
Path_to_save = "C:/Users/Abhigyan/Desktop/Amol's Plots/"
Catagories = ["hosp_patients", "icu_patients"]
Gdm = Global_Dynamic_Mean()
for cat in Catagory:
    i = 1
    Gdm.Divide_by_max_and_add(frame_size, cat)
    Gdm.Divide_by_frame_size(frame_size)
    Country_Groups = SN.segregate_countries(
        DataFrame_to_be_segregated=Gs.Dataframe_with_countries_as_column)
    for pop_group in SN.density_in_ascending_order:
        name_on_saving = "group " + \
            str(i) + "Global Mean" + str(cat) + ".png"
        Gdm.plot_data_frame(path_to_save=Path_to_save,
                            name_on_saving=name_on_saving, Countries=pop_group)
        i += 1
