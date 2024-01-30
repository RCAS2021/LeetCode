import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    output = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    output.rename(columns={'subject_id': 'cnt'}, inplace=True)
    return output

# reset_index -> https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html