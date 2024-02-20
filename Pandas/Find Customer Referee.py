import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    output = pd.DataFrame({
            "name": customer[(customer["referee_id"].isnull()) | (customer["referee_id"]!= 2)]["name"]
        })
    return output
