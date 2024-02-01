import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    output = employees.merge(employee_uni, 'left', on='id')
    return output[['unique_id', 'name']]