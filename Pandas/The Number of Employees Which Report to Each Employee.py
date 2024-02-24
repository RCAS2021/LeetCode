import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    # Groups employees by reports_to, aggregates reports_count = count(employee_id), average_age = mean(age)
    output = employees.groupby("reports_to", as_index=False).agg(reports_count=("employee_id", "count"), average_age=("age", "mean"))
    # Rounds to 0 decimal places, having added + 0.000001 to prevent errors in rounding
    output.average_age = (output.average_age + 1e-6).round(0)
    # Left joins output and employees on left = reports_to and right = employee_id, then renames the column reports_to to employee_id
    output = output.merge(employees, how="left", left_on="reports_to", right_on="employee_id").rename(columns={"reports_to": "employee_id"})
    # Returns the desired columns
    return output[["employee_id", "name", "reports_count", "average_age"]]
