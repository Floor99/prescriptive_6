import pandas as pd


def select_engines_for_maintenance(RUL: pd.DataFrame, max_rul: int):
    RUL_filtered = RUL[RUL["RUL"] <= max_rul]
    return RUL_filtered