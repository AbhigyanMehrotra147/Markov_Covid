from decimal import MAX_EMAX
from Super_class_for_normalization import Super_Normalization as SN
import pandas as pd
import matplotlib.pyplot as plt


class Local_Dynamic(SN):
    def __init__(self, catagory):
        SN.__init__(self)
        SN.Filter_Column(self)
        SN.Grouping_by_country(self)
        self.catagory = catagory
        self.Dataframe_with_countries_as_column = pd.DataFrame()
        self.max_matrix = None

    def Make_dataframe_with_countries_as_column(self):
        for country in self.group_by_country:
            country_name = str(country[0])
            # Skipping all those countries which only have Nan values
            if country[1][self.catagory].count() == 0:
                continue
            self.Dataframe_with_countries_as_column[country_name] = country[1][self.catagory]

    # Creates the maximum array
    # The maximum array holds :

    def Create_max_array(self, frame_size):
        row_size = self.Dataframe_with_countries_as_column.shape[0]
        column_size = self.Dataframe_with_countries_as_column.shape[1]
        self.max_matrix = [[0]*column_size]*row_size
        for i in range(0, row_size):
            # print(self.max_matrix)
            for j in range(0, column_size):
                if i > row_size-frame_size:
                    local_frame_max = self.Dataframe_with_countries_as_column.iloc[i:row_size, j].max(
                    )
                    for k in range(i, frame_size):
                        if self.max_matrix[k][j] < local_frame_max:
                            self.max_matrix[k][j] = local_frame_max
                    continue
                for k in range(i, i+frame_size):
                    local_frame_max = self.Dataframe_with_countries_as_column.iloc[
                        i:i+frame_size+1, j].max()
                    if self.max_matrix[k][j] < local_frame_max:
                        self.max_matrix[k][j] = local_frame_max
        print(self.max_matrix)

    # Functoin divides each data point by the global maximum
    # uses the applymap method which acts on each data point in the data set

    def Divide_by_max_array(self):
        row_size = self.Dataframe_with_countries_as_column.shape[0]
        column_size = self.Dataframe_with_countries_as_column.shape[1]
        for i in range(0, row_size):
            for j in range(0, column_size):
                self.Dataframe_with_countries_as_column.iloc[i,
                                                             j] = self.Dataframe_with_countries_as_column.iloc[i, j]/self.max_matrix[i][j]
        print(self.Dataframe_with_countries_as_column)

    # Function to be made much better in futrue
    # Function plots the new cases from each country normalized to the global maximum
    def plot_data_frame(self):
        plt.plot(self.Dataframe_with_countries_as_column)
        plt.title("Normalizing each country with Dynaamic Local Maximums")
        plt.xlabel("Dates")
        plt.ylabel("Normalized to 1")
        plt.show()


Catagory = ["new_cases", "new_deaths", "hosp_patients", "icu_patients"]
Gd = Local_Dynamic(Catagory[0])
Gd.Make_dataframe_with_countries_as_column()
Gd.Create_max_array(60)
Gd.Divide_by_max_array()
Gd.plot_data_frame()