
import pandas as pd


class Super_Normalization():
    url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'

    def __init__(self):
        self.data_frame = pd.read_csv(Super_Normalization.url)
        self.group_by_country = ()

    def Filter_Column(self):
        filt = self.data_frame.continent == "Europe"
        self.data_frame = self.data_frame.loc[filt]
        self.data_frame.set_index("date", inplace=True)
        self.data_frame.rename(columns={"location": "country"}, inplace=True)
        self.data_frame = self.data_frame[[
            "country", "new_cases", "new_deaths", "hosp_patients", "icu_patients"]]

    def Grouping_by_country(self):
        self.group_by_country = self.data_frame.groupby("country")


Sp = Super_Normalization()
Sp.Filter_Column()
Sp.Grouping_by_country()
