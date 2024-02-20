import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    output = sales.merge(product, on="product_id")
    return output[["product_name", "year", "price"]]
