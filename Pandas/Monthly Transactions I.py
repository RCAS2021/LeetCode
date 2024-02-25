import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    # Transforms trans_date from 2019-01-01 to 2019-01, for example
    transactions['month'] = transactions['trans_date'].apply(lambda x: x.strftime('%Y-%m'))

    # Gets total amounts (total trans amount and total trans count)
    full = transactions.groupby(["country", "month"], dropna=False).agg(trans_total_amount=("amount", "sum"), trans_count=("state", "count")).reset_index()
    # Gets approved amounts (total approved trans amount and approved trans count)
    approved = transactions[transactions["state"] == "approved"].groupby(["country", "month"], dropna=False).agg(approved_count=("id", "count"), approved_total_amount=("amount", "sum")).reset_index()
    # Left joins full and approved on index
    transactions = full.merge(approved, on=None, how="left")
    # Fills NaN approved counts and approved total amounts
    transactions[["approved_count", "approved_total_amount"]] = transactions[["approved_count", "approved_total_amount"]].fillna(0)

    # Returns desired columns
    return transactions[["month", "country", "trans_count", "approved_count", "trans_total_amount", "approved_total_amount"]]
