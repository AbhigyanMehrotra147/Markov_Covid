from decimal import MAX_EMAX
from Super_class_for_normalization import Super_Normalization as SN
import pandas as pd
import matplotlib.pyplot as plt


class Local_Dynamic(SN):
    def __init__(self, catagory):
        SN.__init__(self)
        self.catagory = catagory
        self.Dataframe_with_countries_as_column = SN.get_final_df_Dictionary(self)[self.catagory]
        self.max_matrix = None
        self.row_size = self.Dataframe_with_countries_as_column.shape[0]
        self.column_size = self.Dataframe_with_countries_as_column.shape[1]

    # Creates the maximum array
    # The maximum array holds local maximum for all the frames that a particular 
    # data point was unders corresponding to a particular date (row) and countrie (column) 
    def Create_max_array(self, frame_size): 

        # matrix of row_size * column_size (row * column)
        self.max_matrix = [[0]*self.column_size]*self.row_size

        for i in range(0, self.row_size):
            for j in range(0, self.column_size):

                # condition for the last frame
                if i > self.row_size-frame_size:
                    local_frame_max = self.Dataframe_with_countries_as_column.iloc[i:self.row_size, j].max()
                    for k in range(i, frame_size):
                        if self.max_matrix[k][j] < local_frame_max:
                            self.max_matrix[k][j] = local_frame_max
                    continue

                # updates the matrix with the overall local max 
                # This overall local max is out of all the local max for various frames that a particular data point was under.
                for k in range(i, i+frame_size):
                    local_frame_max = self.Dataframe_with_countries_as_column.iloc[i:i+frame_size+1, j].max()
                    if self.max_matrix[k][j] < local_frame_max:
                        self.max_matrix[k][j] = local_frame_max
       

    # The function divides each data point by the overall local country's max. 
    def Divide_by_max_array(self):

        for i in range(0, self.row_size):
            for j in range(0, self.column_size):
                self.Dataframe_with_countries_as_column.iloc[i,j] = self.Dataframe_with_countries_as_column.iloc[i, j]/self.max_matrix[i][j]

    # Function plots the new cases from each country normalized to the overal local maximum
     def plot_data_frame(self, countries=None):
        super().plot_data_frame(self.Dataframe_with_countries_as_column, "Local Dynamic", self.catagory, countries)


Catagory = ["new_cases", "new_deaths", "hosp_patients", "icu_patients"]
Ld = Local_Dynamic(Catagory[0])
Ld.Create_max_array(60)
Ld.Divide_by_max_array()
Ld.plot_data_frame()