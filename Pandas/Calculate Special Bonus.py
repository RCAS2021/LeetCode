# With fillna !Slower
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.loc[(employees['employee_id'] % 2 != 0) & (employees['name'].str.match(r'(^[^M])')), ['salary']]
    employees = employees[['employee_id', 'bonus']].fillna(0)
    return employees.sort_values(by='employee_id')

# Without fillna !Faster
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0
    employees.loc[(employees['employee_id'] % 2 != 0) & (employees['name'].str.match(r'(^[^M])')), 'bonus'] = employees['salary']
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')