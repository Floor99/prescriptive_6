import pandas as pd


def select_engines_for_maintenance(RUL: pd.DataFrame, max_rul: int):
    """
    Select engines for maintenance based on their Remaining Useful Life (RUL).

    Parameters:
    - RUL (pd.DataFrame): DataFrame containing RUL predictions for engines.
    - max_rul (int): Maximum RUL for engines to be selected for maintenance.

    Returns:
    - pd.DataFrame: DataFrame containing engines selected for maintenance with RUL not exceeding max_rul.
    """
    
    RUL_filtered = RUL[RUL["RUL"] <= max_rul]
    return RUL_filtered