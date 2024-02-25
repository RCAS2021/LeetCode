import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    # Gets sales where sales year = min(year) from sales groupped by product_id, then renames the column year to first_year
    output = sales[sales["year"] == sales.groupby("product_id")["year"].transform("min")].rename(columns={"year": "first_year"})

    # Returns the desired columns
    return output[["product_id", "first_year", "quantity", "price"]]
