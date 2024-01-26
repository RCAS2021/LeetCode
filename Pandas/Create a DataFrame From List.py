import pandas as pd

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    columns_ = ['student_id', 'age']
    result = pd.DataFrame(student_data, columns = columns_)
    return result