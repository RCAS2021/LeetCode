import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    # Merges employee and bonus on primary key empId, using left join (keeps all records from left)
    output = employee.merge(bonus, on="empId", how="left")
    # Gets bonuses lower than 1000 or nan
    output = output[(output["bonus"] < 1000) | (output["bonus"].isna())]
    # Returns name and bonus columns
    return output[["name", "bonus"]]
