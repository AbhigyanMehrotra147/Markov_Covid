from Super_class_for_normalization import Super_Normalization as SN
import pandas as pd
import matplotlib.pyplot as plt


class Local_Static(SN):
    # Initiializing super class and this class
    # Also assiging a catagory such as 'new_cases'
    def __init__(self, catagory):
        SN.__init__(self)
        self.catagory = catagory
        self.Dataframe_with_countries_as_column = SN.get_final_df_Dictionary(self)[
            self.catagory]

    # Functoin divides each data point by the local maximum
    # uses the applymap method which acts on each data point in the data set

    def Divide_by_global_max(self):
        for column in self.Dataframe_with_countries_as_column:
            local_max = self.Dataframe_with_countries_as_column[column].max()
            self.Dataframe_with_countries_as_column[column] = self.Dataframe_with_countries_as_column[column].apply(
                lambda x: x/local_max)

    # Function to be made much better in futrue
    # Function plots the new cases from each country normalized to the global maximum

    def plot_data_frame(self, countries=None):
        super().plot_data_frame(
            self.Dataframe_with_countries_as_column, "Local Static", self.catagory, countries)


Catagory = ["new_cases", "new_deaths", "hosp_patients", "icu_patients"]
country = ['Germany', 'France', 'Italy']
Ls = Local_Static(Catagory[0])
Ls.Divide_by_global_max()
Ls.plot_data_frame()
