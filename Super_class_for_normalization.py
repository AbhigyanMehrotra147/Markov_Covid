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
        
    
    #storing the list of countries with whole column as empty values for a specific parameter    
    def list_of_Nan_countries(self,parameter):
        
        array_of_null_countries = []
       
        for grouped_country_name, grouped_country_database in self.group_by_country:
            if (len(grouped_country_database) == grouped_country_database[parameter].isnull().sum()):
                array_of_null_countries.append(grouped_country_name)
        return array_of_null_countries

    
    #dataframe of countries for a particular parameter in the form of Pivot Table   
    def get_country_df_for_particular_parameter(self,parameter):
        country_df_particular_parameter = self.data_frame.pivot(index = "date", columns = "country", values = parameter)
        return country_df_particular_parameter
    
    
    #remove the columns of the list of Nan countries from the dataframe
    def delete_Nan_countries_from_df (self, array_of_null_countries, country_df_particular_parameter ):
        
        for df_country in country_df_particular_parameter.columns:
            for array_country in array_of_null_countries:
                if array_country in df_country:
                    del country_df_particular_parameter[df_country]
        return country_df_particular_parameter
    
    
    #storing the name of the parameters from the data frame of a list
    def getparameter_array(self):
        col_array = []
        for col_name in self.data_frame.columns:
            if(col_name != "date" and col_name != "country"):
                col_array.append(col_name)
        return col_array
    
    #returns the final clean dataset for each parameter in the form of dictionary
    #where the parameter are the keys and data frames are the values
    
 
    def get_final_df_Dictionary(self):
        self.Filter_Column()
        self.data_frame.reset_index(inplace =True)
        self.Grouping_by_country()
        dictionary = {}
        col_array = df.getparameter_array()
        for parameter in col_array:
            Nan_ans = self.list_of_Nan_countries(parameter)
            df_ans = self.get_country_df_for_particular_parameter(parameter)
            deleted_nan_country_df = self.delete_Nan_countries_from_df(Nan_ans, df_ans)
            #final missing values "inside" the dataframe are filled using linear interpolation method
            dictionary[parameter] = deleted_nan_country_df.interpolate(limit_area = "inside")
            
        return dictionary
        
# Sp = Super_Normalization()
# #you are access the dataframe for each the four parameter by just using passing parameter as the key value
# #in the dictionary
# dict = Sp.get_final_df_Dictionary()
