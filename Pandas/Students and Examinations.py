import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    output = students.merge(subjects, 'cross')
    cnt = examinations.groupby(['student_id', 'subject_name']).agg(attended_exams=('subject_name', 'count')).reset_index()
    output = output.merge(cnt, on=['student_id', 'subject_name'], how='left')
    output = output.sort_values(by=['student_id', 'subject_name'])
    output['attended_exams'] = output['attended_exams'].fillna(0)

    return output[['student_id', 'student_name', 'subject_name', 'attended_exams']]