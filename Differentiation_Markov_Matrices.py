import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from Super_class_for_normalization import Super_Normalization as SN
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

path_for_differentiated_dataframe = "C:/Users/Abhigyan/Desktop/First_Derivative_Rolling_Average_28_days/GDM_new_deaths.pickle"
name_to_save_plot = ""
path_to_save_plots = "C:/Users/Abhigyan/Desktop/First_Derivative_Rolling_Average_28_days/Plots_new_deaths/"
Datafame = pd.read_pickle(path_for_differentiated_dataframe)

# SN.plot_data_frame(Datafame, path_to_save=path_to_save_plots,
#                    name_on_saving=name_to_save_plot, countries=[])

# Saving Graph for each country
name_to_save_plot = "Gdm_new_deaths"
for country in Datafame.columns:
    name_to_save_plot_temp = name_to_save_plot+country
    SN.plot_data_frame(Datafame, path_to_save=path_to_save_plots,
                       name_on_saving=name_to_save_plot_temp, countries=[country])
