import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    # Gets employees with salaries less than 30.000
    output = employees[employees["salary"] < 30000]
    # Gets employees where manager_id doesn't exist in employee_id and not NaN values
    output = output[
        (~output["manager_id"].isin(employees["employee_id"]))
          &
        (output["manager_id"].notna())
        ]

    # Return employee_id column sorted by employee_id
    return output[["employee_id"]].sort_values("employee_id")
