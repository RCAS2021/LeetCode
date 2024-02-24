import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    # one_dep will receive the rows where employees have only one department (includes those where primary_flag = "N")
    one_dep = employee
    # Creates and transforms count column to receive the deparment_id count per employee_id
    one_dep["count"] = employee.groupby(["employee_id"])["department_id"].transform("count")
    # Receives only the rows where count == 1
    one_dep = one_dep[one_dep["count"] == 1]

    # Primary will receive the rows where primary_flag = "Y" from employees
    primary = employee[employee["primary_flag"] == "Y"]

    # Concat both one_dep and primary to receive the employees where primary_flag = "Y",
    # and those who have one department and because of that, didn't choose a primary department, then having primary_flag = "N"
    merged = pd.concat([one_dep, primary])

    # Return the expected columns and drops duplicates,
    # preventing having employees who chose to have a primary_flag but don't belong to two departments
    return merged[["employee_id", "department_id"]].drop_duplicates()
