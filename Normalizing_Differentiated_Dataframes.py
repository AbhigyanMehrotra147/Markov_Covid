import pandas as pd
from Color_file import DataFrame
from Super_class_for_normalization import Super_Normalization as SN
Path_for_Data_frame = "C:/Users/Abhigyan/Desktop/First_Derivative_Rolling_Average_28_days/Second_Derivative/Rolling_Average/GDM_new_deaths.pickle"
Dataframe = pd.read_pickle(Path_for_Data_frame)


def Divide_by_max_min(Dataframe, x, country="Germany"):
    positive = float(Dataframe[country].min())
    negative = float(Dataframe[country].max())
    if abs(negative) > positive:
        Max = abs(negative)
    if positive >= abs(negative):
        Max = positive
    return round(x/Max, 3)


def Normalize(Dataframe):
    for country in Dataframe.columns:
        Dataframe[country] = Dataframe[country].apply(
            lambda x: Divide_by_max_min(Dataframe=Dataframe, x=x, country=country))
        Dataframe.to_pickle(
            "C:/Users/Abhigyan/Desktop/First_Derivative_Rolling_Average_28_days/Second_Derivative/Rolling_Average/Normalized/Gdm_new_deaths.pickle")
    return Dataframe


path_to_save_plots = "C:/Users/Abhigyan/Desktop/First_Derivative_Rolling_Average_28_days/Second_Derivative/Rolling_Average/Normalized/Plots_new_deaths/"
name_to_save_plot_ = "Gdm_"


def plot(Dataframe):
    for country in Dataframe.columns:
        name_to_save_plot_temp = name_to_save_plot_+country
        SN.plot_data_frame(DathFrame_to_be_plotted=Dataframe, path_to_save=path_to_save_plots,
                           name_on_saving=name_to_save_plot_temp, countries=[country])


Dataframe = Normalize(Dataframe=Dataframe)
plot(Dataframe=Dataframe)
