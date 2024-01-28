import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(department, left_on='departmentId', right_on='id')
    merged = merged.rename(columns={'name_x': 'Employee', 'name_y': 'Department', 'salary': 'Salary'})[['Department', 'Employee', 'Salary']]

    return merged[merged.Salary == merged.groupby('Department')['Salary'].transform(max)]

# transform -> https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transform.html