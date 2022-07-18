
from Super_class_for_normalization import Super_Normalization as SN
import pandas as pd
import matplotlib.pyplot as plt


class Global_Static(SN):
    # Initiailizig super class and this class
    # also assigning a catagory to each instant. Such as 'new_cases'
    def __init__(self):
        SN.__init__(self)
        self.Dataframe_with_countries_as_column = pd.DataFrame()
        self.Dataframe_dictionary = SN.get_final_df_Dictionary(self)

    # Functoin divides each data point by the global maximum
    # uses the applymap method which acts on each data point in the data set

    def Divide_by_global_max(self, catagory):
        # Creating a deep copy because we dont want changes to reflect in the original dataframe
        # Assigning cataogry to Dataframe_with_countries_as_column
        self.Dataframe_with_countries_as_column = self.Dataframe_dictionary[catagory].copy(
            deep=True)
        global_max = self.Dataframe_with_countries_as_column.max().max()
        self.Dataframe_with_countries_as_column = self.Dataframe_with_countries_as_column.applymap(
            lambda x: x/global_max)

    # Function to be made much better in futrue
    # Function plots the new cases from specified country normalized to the global maximum
    def plot_data_frame(self, path_to_save="", Countries=None, name_on_saving=""):
        super().plot_data_frame(
            DathFrame_to_be_plotted=self.Dataframe_with_countries_as_column, countries=Countries, path_to_save=path_to_save, name_on_saving=name_on_saving)


Catagories = ["new_cases", "new_deaths", "hosp_patients", "icu_patients"]
Gs = Global_Static()
Path_to_save = "C:/Users/Abhigyan/Desktop/Amol's Plots/"
for cat in Catagories:
    i = 1
    Gs.Divide_by_global_max(catagory=cat)
    Country_Groups = SN.segregate_countries(
        DataFrame_to_be_segregated=Gs.Dataframe_with_countries_as_column)
    for pop_group in Country_Groups:
        name_on_saving = "group " + \
            str(i) + "Global Static " + str(cat) + ".png"
        Gs.plot_data_frame(path_to_save=Path_to_save,
                           name_on_saving=name_on_saving, Countries=pop_group)
        i += 1
