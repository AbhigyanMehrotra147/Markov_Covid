from abc import ABC, abstractmethod


class Format_For_File(ABC):
    # Filtering columns based on requirements
    @abstractmethod
    def Filter_Column(self):
        pass
    # Specific cretira to manipulate data_frame
    # Such as Global Maximum

    @abstractmethod
    def Set_Criteria(self):
        pass
    # Creation of the new data frame according to the filter and criteria

    @abstractmethod
    def Make_new_data_fram(self):
        pass
    # Customizing plotting according to the dataframe

    @abstractmethod
    def Plot_data_frame(self):
        pass
