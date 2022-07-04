from Super_class_for_normalization import Super_Normalization as SN
import pandas as pd
import matplotlib.pyplot as plt


class Local_Static(SN):
    def __init__(self, catagory):
        SN.__init__(self)
        SN.Filter_Column(self)
        SN.Grouping_by_country(self)
        self.catagory = catagory
        self.Dataframe_with_countries_as_column = pd.DataFrame()

    def Make_dataframe_with_countries_as_column(self):
        for country in self.group_by_country:
            country_name = str(country[0])
            # Skipping all those countries which only have Nan values
            if country[1][self.catagory].count() == 0:
                continue
            self.Dataframe_with_countries_as_column[country_name] = country[1][self.catagory]

    # Functoin divides each data point by the global maximum
    # uses the applymap method which acts on each data point in the data set

    def Divide_by_global_max(self):
        for column in self.Dataframe_with_countries_as_column:
            local_max = self.Dataframe_with_countries_as_column[column].max()
            self.Dataframe_with_countries_as_column[column] = self.Dataframe_with_countries_as_column[column].apply(
                lambda x: x/local_max)
        # print(self.Dataframe_with_countries_as_column)
    # Function to be made much better in futrue
    # Function plots the new cases from each country normalized to the global maximum

    def plot_data_frame(self):
        plt.plot(self.Dataframe_with_countries_as_column)
        plt.title("Normalizing each country with Local Maximum")
        plt.xlabel("Dates")
        plt.ylabel("Normalized to 1")
        plt.show()


Catagory = ["new_cases", "new_deaths", "hosp_patients", "icu_patients"]
Ls = Local_Static(Catagory[0])
Ls.Make_dataframe_with_countries_as_column()
Ls.Divide_by_global_max()
Ls.plot_data_frame()
