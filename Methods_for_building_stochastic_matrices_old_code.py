import numpy as np
import pandas as pd
# Conversion of the dataframe into three states


@staticmethod
def num_to_sign_converter(val, Max=1):

    if val <= Max/3:
        # assign the value - (mild)
        return "-"

    elif val > Max/3 and val <= (2/3)*Max:
        # assign the value + (moderate)
        return "+"

    elif Max/val > (2/3)*Max and val <= Max:
        # assign the value ++ (severe)
        return "++"
    else:
        return np.nan

# Conversion of the dataframe into five states


@staticmethod
def num_to_sign_converter_into_five_states(val, Max=1):

    if val <= Max/5:
        # assign the value -- (very mild)
        return "--"

    elif val > Max/5 and val <= (2/5)*Max:
        # assign the value - (mild)
        return "-"

    elif val > (2/5)*Max and val <= (3/5)*Max:
        # assign the value o (moderate)
        return "o"
    elif val > (3/5)*Max and val <= (4/5)*Max:
        # assign the value o (severe)
        return "+"
    elif val > (4/5)*Max and val <= Max:
        # assign the value "++" (very severe)
        return "++"
    else:
        return np.nan
# Saving Dataframe as pickle file
# Converting DataFrame to Three_states


@staticmethod
def save_and_convert_to_three_states_with_max_1(dataframe, file_name):
    Three_states_df = dataframe.applymap(
        lambda x: num_to_sign_converter(x))
    print(Three_states_df)
    Three_states_df.to_excel(file_name + ".pickle")


@staticmethod
def save_and_convert_to_state_with_country_specific_max(dataframe, file_name, time_period=7):
    states_df = pd.DataFrame()
    for country in dataframe.columns:
        max_of_country = dataframe[country].max()
        states_df[country] = dataframe[country].apply(
            lambda x: num_to_sign_converter(x, max_of_country))
    Averaged_states_df = take_average_of_state(
        states_df, Time_period=time_period)
    Averaged_states_df.to_pickle(file_name + ".pickle")
    Averaged_states_df.to_excel(file_name+".xlsx")
    # states_df.to_pickle(file_name+".pickle")

# Function adds one to entry corresponding to specific state to state transfer for three states


@staticmethod
def assign_transition(state_a, state_b, Stochastic_matrix):
    if state_a == '-' and state_b == '-':
        Stochastic_matrix[0][0] += 1
    if state_a == '-' and state_b == '+':
        Stochastic_matrix[0][1] += 1
    if state_a == '-' and state_b == '++':
        Stochastic_matrix[0][2] += 1
    if state_a == '+' and state_b == '-':
        Stochastic_matrix[1][0] += 1
    if state_a == '+' and state_b == '+':
        Stochastic_matrix[1][1] += 1
    if state_a == '+' and state_b == '++':
        Stochastic_matrix[1][2] += 1
    if state_a == '++' and state_b == '-':
        Stochastic_matrix[2][0] += 1
    if state_a == '++' and state_b == '+':
        Stochastic_matrix[2][1] += 1
    if state_a == '++' and state_b == '++':
        Stochastic_matrix[2][2] += 1


@staticmethod
def assign_transition_to_five_states(state_a, state_b, stochastic_matrix):
    if state_a == '--':
        if state_b == '--':
            stochastic_matrix[0][0] += 1
        elif state_b == '-':
            stochastic_matrix[0][1] += 1
        elif state_b == 'o':
            stochastic_matrix[0][2] += 1
        elif state_b == '+':
            stochastic_matrix[0][3] += 1
        elif state_b == '++':
            stochastic_matrix[0][4] += 1
    if state_a == '-':
        if state_b == '--':
            stochastic_matrix[1][0] += 1
        elif state_b == '-':
            stochastic_matrix[1][1] += 1
        elif state_b == 'o':
            stochastic_matrix[1][2] += 1
        elif state_b == '+':
            stochastic_matrix[1][3] += 1
        elif state_b == '++':
            stochastic_matrix[1][4] += 1
    if state_a == 'o':
        if state_b == '--':
            stochastic_matrix[2][0] += 1
        elif state_b == '-':
            stochastic_matrix[2][1] += 1
        elif state_b == 'o':
            stochastic_matrix[2][2] += 1
        elif state_b == '+':
            stochastic_matrix[2][3] += 1
        elif state_b == '++':
            stochastic_matrix[2][4] += 1
    if state_a == '+':
        if state_b == '--':
            stochastic_matrix[3][0] += 1
        elif state_b == '-':
            stochastic_matrix[3][1] += 1
        elif state_b == 'o':
            stochastic_matrix[3][2] += 1
        elif state_b == '+':
            stochastic_matrix[3][3] += 1
        elif state_b == '++':
            stochastic_matrix[3][4] += 1
    if state_a == '++':
        if state_b == '--':
            stochastic_matrix[4][0] += 1
        elif state_b == '-':
            stochastic_matrix[4][1] += 1
        elif state_b == 'o':
            stochastic_matrix[4][2] += 1
        elif state_b == '+':
            stochastic_matrix[4][3] += 1
        elif state_b == '++':
            stochastic_matrix[4][4] += 1


@staticmethod
# Assigns numeric values to states
def assign_value_to_state(state):
    if state == '-':
        return -1
    if state == '+':
        return 0
    if state == '++':
        return 1


@staticmethod
def convert_numeric_value_to_state(number):
    if number <= 1.1 and number > 0.33:
        return '-'
    if number <= 0.33 and number > -0.33:
        return '+'
    if number <= -0.33 and number > -1.1:
        return '++'


@staticmethod
# Takes the average of states in a dataframe
# The average is taken on specific time period
def take_average_of_state(DataFrame=pd.DataFrame(), Time_period=7):
    State_with_numeric_values = DataFrame.copy(deep=True)
    State_with_numeric_values = State_with_numeric_values.applymap(
        lambda x: assign_value_to_state(x))
    No_of_rows = State_with_numeric_values.shape[0]
    Averaged_State_dataFrame = pd.DataFrame()
    for i in range(0, No_of_rows-Time_period, Time_period):
        Averaged_State_dataFrame = Averaged_State_dataFrame.append(
            State_with_numeric_values.iloc[i:i+Time_period].mean(), ignore_index=True)
    Averaged_State_dataFrame = Averaged_State_dataFrame.applymap(
        lambda x: convert_numeric_value_to_state(x))

    print(Averaged_State_dataFrame["Germany"][0:60])
    return Averaged_State_dataFrame

# Builds the stochastic matrix


@staticmethod
def get_transition_matrix(dataframe=pd.DataFrame(), Country="Germany", size=3):
    for j in range(0, dataframe.shape[1]):
        if dataframe.columns[j] == Country:
            column_index = j
            break
    Numb_rows = dataframe.shape[0]
    Stochastic_Matrix = [[0]*size]*size
    Stochastic_Matrix_np = np.array(Stochastic_Matrix)
    for i in range(0, Numb_rows-1):
        assign_transition_to_five_states(
            state_a=dataframe.iloc[i, column_index], state_b=dataframe.iloc[i+1, column_index], stochastic_matrix=Stochastic_Matrix_np)
    sum_of_rows = np.sum(Stochastic_Matrix_np, 1)
    Stochastic_Matrix_np = Stochastic_Matrix_np.astype(np.float16)
    for m in range(size):
        for n in range(size):
            if sum_of_rows[m] == 0:
                continue
            Stochastic_Matrix_np[m][n] = round(Stochastic_Matrix_np[m][n] /
                                               sum_of_rows[m], 3)
    return Stochastic_Matrix_np
