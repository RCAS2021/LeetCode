import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    output = visits.merge(transactions, on="visit_id", how="outer")
    output = output[
        output["transaction_id"].isna()
        ].groupby("customer_id").count().reset_index().rename(
            {
            "visit_id": "count_no_trans"
            }, axis="columns")
    return output[["customer_id", "count_no_trans"]]
