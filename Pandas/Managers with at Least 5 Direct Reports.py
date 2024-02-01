import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    output = employee.groupby('managerId')['id'].count().reset_index()
    output = output.loc[output['id'] > 4]
    output = output.merge(employee[['id', 'name']], left_on='managerId', right_on='id', how='inner')
    return output[['name']]