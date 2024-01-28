import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:   
    employee = employee.drop_duplicates('salary', keep='first').sort_values(by='salary', ascending=False)
    if N > len(employee) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    return pd.DataFrame({f'getNthHighestSalary({N})': [employee.iloc[N - 1]['salary']]})