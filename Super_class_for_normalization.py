
import pandas as pd
import matplotlib.pyplot as plt


class Super_Normalization():
    # Declaring static url of data
    url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
    # Declaring standard colors for all countries. These colors will be fixed across all plots
    COLOR = {'France': '#44a2c7', 'Germany': '#f42fa2', 'Finland': '#3b2b99', 'Russia': '#f41f09', 'United Kingdom': '#a25ee1', 'Italy': '#91190a', 'Spain': '#0258bb', 'Sweden': '#2f65bf', 'Slovenia': '#d2ba0d', 'Denmark': '#a83e40', 'Estonia': '#8d3b08', 'Belgium': '#9dbeaa', 'Greece': '#5e4b98', 'Luxembourg': '#b51c57', 'Norway': '#1e5c3e', 'Switzerland': '#2106f2', 'Albania': '#53ace0', 'Austria': '#223406', 'Croatia': '#4f5026', 'Latvia': '#c923cc', 'Romania': '#ae7a50', 'North Macedonia': '#59a61f', 'Serbia': '#96510b', 'Netherlands': '#0525ba', 'Belarus': '#bc6309', 'Iceland': '#e2d4b3',
             'Monaco': '#c28cc5', 'Ireland': '#62b93e', 'San Marino': '#668d02', 'Czechia': '#bcaab2', 'Portugal': '#4851de', 'Andorra': '#c6d06f', 'Ukraine': '#5a7c84', 'Hungary': '#1d9d53', 'Liechtenstein': '#b3a9c0', 'Faeroe Islands': '#d2eef6', 'Poland': '#a55d32', 'Gibraltar': '#bfa438', 'Bosnia and Herzegovina': '#e3cad7', 'Malta': '#2346a6', 'Slovakia': '#732bc8', 'Vatican': '#e52e53', 'Moldova': '#998396', 'Cyprus': '#400089', 'Bulgaria': '#fbe7a8', 'Kosovo': '#f2c023', 'Montenegro': '#a2c1bd', 'Lithuania': '#18a424', 'Isle of Man': '#4a1793', 'Guernsey': '#171d71', 'Jersey': '#256586'}

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

    # storing the list of countries with whole column as empty values for a specific parameter

    def list_of_Nan_countries(self, parameter):

        array_of_null_countries = []

        for grouped_country_name, grouped_country_database in self.group_by_country:
            if (len(grouped_country_database) == grouped_country_database[parameter].isnull().sum()):
                array_of_null_countries.append(grouped_country_name)
        return array_of_null_countries

    # dataframe of countries for a particular parameter in the form of Pivot Table

    def get_country_df_for_particular_parameter(self, parameter):
        country_df_particular_parameter = self.data_frame.pivot(
            index="date", columns="country", values=parameter)
        return country_df_particular_parameter

    # remove the columns of the list of Nan countries from the dataframe

    def delete_Nan_countries_from_df(self, array_of_null_countries, country_df_particular_parameter):

        for df_country in country_df_particular_parameter.columns:
            for array_country in array_of_null_countries:
                if array_country in df_country:
                    del country_df_particular_parameter[df_country]
        return country_df_particular_parameter

    # storing the name of the parameters from the data frame of a list

    def getparameter_array(self):
        col_array = []
        for col_name in self.data_frame.columns:
            if(col_name != "date" and col_name != "country"):
                col_array.append(col_name)
        return col_array

    # returns the final clean dataset for each parameter in the form of dictionary
    # where the parameter are the keys and data frames are the values

    def get_final_df_Dictionary(self):
        self.Filter_Column()
        self.data_frame.reset_index(inplace=True)
        self.Grouping_by_country()
        dictionary = {}
        col_array = self.getparameter_array()
        for parameter in col_array:
            Nan_ans = self.list_of_Nan_countries(parameter)
            df_ans = self.get_country_df_for_particular_parameter(parameter)
            deleted_nan_country_df = self.delete_Nan_countries_from_df(
                Nan_ans, df_ans)
            # final missing values "inside" the dataframe are filled using linear interpolation method
            dictionary[parameter] = deleted_nan_country_df.interpolate(
                limit_area="inside")

        return dictionary

    # The Type argument is the type of Normalization
    # The catagory argument is a catagory such as 'new_cases'
    # The countries = None arguments plots all countries if there are no specified countries
    def plot_data_frame(self, DataFrame, Type, catagory, countries=None):
        DataFrame.reset_index(inplace=True)
        DataFrame['date'] = pd.to_datetime(DataFrame['date'])

        if countries != None:
            for column in countries:
                plt.plot(
                    DataFrame.date, DataFrame[column], color=Super_Normalization.COLOR[column], label=column)
        if countries == None:
            for column in DataFrame:
                if column == 'date':
                    continue
                plt.plot(
                    DataFrame['date'], DataFrame[column], color=Super_Normalization.COLOR[column], label=column)
        plt.title("Normalizing each country with " +
                  Type + " Maximum " + catagory)
        plt.xlabel("Dates")
        plt.ylabel("Normalized to 1")
        plt.legend(bbox_to_anchor=(1, 1), loc='upper left')
        plt.show()
# Sp = Super_Normalization()
# #you are access the dataframe for each the four parameter by just using passing parameter as the key value
# #in the dictionary
# dict = Sp.get_final_df_Dictionary()
# import pandas as pd
