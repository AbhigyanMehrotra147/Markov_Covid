import pandas as pd
import Super_class_for_normalization as SN

Excel_data_frame = ""
Path_to_save_dataframe = "C:/Users/Abhigyan/Desktop/Matrices_of_states/global_dynamic_mean_new_cases_no_avg.csv "
Excel_File = pd.read_excel(
    Excel_data_frame)
Excel_File.to_csv(Path_to_save_dataframe, index=None, header=True)
DataFrame = pd.read_csv(Path_to_save_dataframe)
Stochastic_Matrix = SN.Super_Normalization.get_transition_matrix(
    dataframe=DataFrame, Country="France")
print(Stochastic_Matrix)
