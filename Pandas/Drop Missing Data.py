import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=['name'], axis = 0)

# dropna() -> https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html