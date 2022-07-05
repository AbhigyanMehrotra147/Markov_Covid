from Super_class_for_normalization import Super_Normalization as SN
import pandas as pd
import matplotlib.pyplot as plt


class Global_Static(SN):
    # Initiailizig super class and this class
    # also assigning a catagory to each instant. Such as 'new_cases'
    def __init__(self, catagory):
        SN.__init__(self)
        self.catagory = catagory
        self.Dataframe_with_countries_as_column = SN.get_final_df_Dictionary(self)[
            self.catagory]

    # Function divides each data point by the global maximum
    # uses the applymap method which acts on each data point in the data set

    def Divide_by_global_max(self):
        global_max = self.Dataframe_with_countries_as_column.max().max()
        self.Dataframe_with_countries_as_column = self.Dataframe_with_countries_as_column.applymap(lambda x: x/global_max)

    # Function to be made much better in future
    # Function plots the new cases from each country normalized to the global maximum

    def plot_data_frame(self):
        plt.plot(self.Dataframe_with_countries_as_column)
        plt.title("Normalizing each country with Global Maximum")
        plt.xlabel("Dates")
        plt.ylabel("Normalized to 1")
        plt.show()


Catagory = ["new_cases", "new_deaths", "hosp_patients", "icu_patients"]
Gs = Global_Static(Catagory[0])
Gs.Divide_by_global_max()
Gs.plot_data_frame()