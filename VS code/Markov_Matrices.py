import pandas as pd
import Super_class_for_normalization as SN

Excel_data_frame = "C:/Users/Abhigyan/Desktop/Covid_Project_connected_to_github/Excel_files_and_csv_files/Global_Dynamic/Without_rolling_average/new_cases.xlsx"
Path_to_save_dataframe = "C:/Users/Abhigyan/Desktop/Covid_Project_connected_to_github/Excel_files_and_csv_files/Global_Dynamic/Without_rolling_average/new_cases_csv.csv"
Excel_File = pd.read_excel(
    Excel_data_frame)
Excel_File.to_csv(Path_to_save_dataframe, index=None, header=True)
DataFrame = pd.read_csv(Path_to_save_dataframe)
DataFrame.set_index('date', inplace=True)
Dictionary_of_Stochastic_Matrices = {}
for country in DataFrame:
    Dictionary_of_Stochastic_Matrices[country] = SN.Super_Normalization.get_transition_matrix(
        dataframe=DataFrame, Country=country)
for country_key in Dictionary_of_Stochastic_Matrices:
    print(country_key, end="\n")
    for row in Dictionary_of_Stochastic_Matrices[country_key]:
        print(row)
    print()
