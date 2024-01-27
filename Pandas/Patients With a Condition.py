import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    patients = patients.loc[patients['conditions'].str.match(r'^DIAB1|.*\sDIAB1')]
    return patients