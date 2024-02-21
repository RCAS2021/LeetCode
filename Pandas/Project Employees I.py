import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    # Left joins project and employee on employee_id
    output = project.merge(employee, on="employee_id", how="left")
    # Drops rows with NaN values
    output = output.dropna()
    # Groups by project_id, aggregating experience_years sum and employee_id count,
    # then assigning average_years to the rounded average by 2 decimal places and resetting the index
    output = output.groupby("project_id").agg({
            "experience_years": "sum",
            "employee_id" : "count"
        }).assign(
            average_years=lambda i: round(i.experience_years / i.employee_id, 2)
        )[["average_years"]].reset_index()
    
    return output
