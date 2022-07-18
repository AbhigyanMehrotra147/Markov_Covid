
from Super_class_for_normalization import Super_Normalization as SN
import pandas as pd
import matplotlib.pyplot as plt


class Local_Static(SN):

    def __init__(self, catagory):
        SN.__init__(self)
        self.catagory = catagory
        self.Dataframe_with_countries_as_column = SN.get_final_df_Dictionary(self)[
            catagory]

    # Function divides each data point in a country column with its maximum value
    def Divide_by_local_max(self):
        for column in self.Dataframe_with_countries_as_column:
            # maximun value found
            local_max = self.Dataframe_with_countries_as_column[column].max()
            # the apply method acts on each column data point in the dataframe (default axis value is 0)
            self.Dataframe_with_countries_as_column[column] = self.Dataframe_with_countries_as_column[column].apply(
                lambda x: x/local_max)

    # Function plots the new cases from each country normalized to the global maximum
    def plot_data_frame(self, population_group, countries=None):
        super().plot_data_frame(
            self.Dataframe_with_countries_as_column, "Local Static", self.catagory, countries, population_group)


Catagory = ["new_cases", "new_deaths", "hosp_patients", "icu_patients"]
for catagory in Catagory:
    i = 1
    for pop_group in SN.population_in_ascending_order:
        Ls = Local_Static(catagory)
        Ls.Divide_by_local_max()
        # print(str(pop_group))
        Ls.plot_data_frame(population_group="group " + str(i)
                           + " ", countries=pop_group)
        i += 1
