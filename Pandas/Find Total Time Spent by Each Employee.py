import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    employees['total_time'] = employees.groupby(['event_day', 'emp_id'])['total_time'].transform(sum)
    employees = employees.drop_duplicates(['total_time', 'event_day'])
    output = pd.DataFrame({'day': employees['event_day'], 'emp_id': employees['emp_id'], 'total_time': employees['total_time']})
    return output