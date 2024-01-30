import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses = courses.groupby('class').count().reset_index()
    output = pd.DataFrame({'class': courses['class'].loc[courses['student'] >= 5]})
    return output