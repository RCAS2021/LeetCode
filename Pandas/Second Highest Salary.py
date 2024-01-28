import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates('salary', keep='first').sort_values(by='salary', ascending=True)
    if len(employee) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    return pd.DataFrame({'SecondHighestSalary': [employee.iloc[-2]['salary']]})