import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype('int')
    return students

# astype -> https://pandas.pydata.org/docs/user_guide/basics.html#astype