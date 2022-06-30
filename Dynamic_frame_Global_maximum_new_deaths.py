from Abstract_for_each_file import Format_For_File as fff
import pandas as pd
import matplotlib.pyplot as plt
URL = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'


class Global_new_deaths(fff):
    def __init__(self, url):
        self.Data_frame = pd.read_csv(url)
        self.criteria = 0
        self.Grouped_location_data_frame = None
        self.Merged_data_frame = pd.DataFrame()
        self.Max_array = [0]*1500

    def Filter_Column(self):
        filt = self.Data_frame.continent == "Europe"
        self.Data_frame = self.Data_frame.loc[filt]
        self.Data_frame.set_index('date', inplace=True)
        self.Data_frame = self.Data_frame[['location', 'new_deaths']]
        self.Data_frame.iloc[0:42954, 1].fillna(0, inplace=True)

    def Set_Criteria(self):
        rows = self.Merged_data_frame.shape[0]
        for i in range(0, rows):
            if i > rows - 121:
                Max = self.Merged_data_frame.iloc[i:rows].max().max()
                for j in range(i, rows):
                    if self.Max_array[j] < Max:
                        self.Max_array[j] = Max
                continue
            Max = self.Merged_data_frame.iloc[i:i+120].max().max()
            for j in range(i, i+120):
                if self.Max_array[j] < Max:
                    self.Max_array[j] = Max

    def Make_new_data_fram(self):
        self.Grouped_location_data_frame = self.Data_frame.groupby([
                                                                   'location'])
        for country in self.Grouped_location_data_frame:
            country_name = str(country[0])
            self.Merged_data_frame[country_name] = country[1]['new_deaths']
            self.Merged_data_frame.fillna(0, inplace=True)
        self.Set_Criteria()
        for i in range(0, self.Merged_data_frame.shape[0]):
            self.Merged_data_frame.iloc[i] = self.Merged_data_frame.iloc[i] / \
                self.Max_array[i]

    def Plot_data_frame(self):
        plt.plot(self.Merged_data_frame)
        plt.title("Dynamic Gloabal maximum Normalized deaths to each country")
        plt.xlabel('Date')
        plt.ylabel(
            'Normalized to Global maximum new cases per Dynamic frame of 120')
        plt.show()
        pass


GNC = Global_new_deaths(URL)
GNC.Filter_Column()
GNC.Make_new_data_fram()
GNC.Plot_data_frame()
