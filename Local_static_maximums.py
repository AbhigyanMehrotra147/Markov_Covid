
from Super_class_for_normalization import Super_Normalization as SN
import pandas as pd
import matplotlib.pyplot as plt


class Local_Static(SN):

    def __init__(self):
        SN.__init__(self)
        # Adding Dataframe Dictionary to make execution faster
        self.Dataframe_dictionary = SN.get_final_df_Dictionary(self)
        # Self.Dataframe_with_countries_as_column will now be assigned value according to catogary in function not inside initializer
        self.Dataframe_with_countries_as_column = pd.DataFrame()
    # Function divides each data point in a country column with its maximum value

    def Divide_by_local_max(self, catagory="new_cases"):
        # Assigning Catagory to Dataframe with countries as column
        # Making a deep copy so that changes do reflect in the original dataframe
        self.Dataframe_with_countries_as_column = self.Dataframe_dictionary[catagory].copy(
            deep=True)
        for column in self.Dataframe_with_countries_as_column:
            # maximun value found
            local_max = self.Dataframe_with_countries_as_column[column].max()
            # the apply method acts on each column data point in the dataframe (default axis value is 0)

            self.Dataframe_with_countries_as_column[column] = self.Dataframe_with_countries_as_column[column].apply(
                lambda x: x/local_max)

    # Function plots the new cases from each country normalized to the local maximum
    def plot_data_frame(self, path_to_save="", Countries=None, name_on_saving=""):
        super().plot_data_frame(
            DathFrame_to_be_plotted=self.Dataframe_with_countries_as_column, countries=Countries, path_to_save=path_to_save, name_on_saving=name_on_saving)


Catagories = ["new_cases", "new_deaths", "hosp_patients", "icu_patients"]
Path_to_save = "C:/Users/Abhigyan/Desktop/Amol's Plots/"
Ls = Local_Static()
for cat in Catagories:
    i = 1
    Ls.Divide_by_local_max(catagory=cat)
    Country_Groups = SN.segregate_countries(
        DataFrame_to_be_segregated=Ls.Dataframe_with_countries_as_column)
    for pop_group in Country_Groups:
        name_on_saving = "group " + \
            str(i) + "Local Static " + str(cat) + ".png"
        Ls.plot_data_frame(path_to_save=Path_to_save,
                           name_on_saving=name_on_saving, Countries=pop_group)
        i += 1
