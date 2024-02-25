import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    date_min = pd.Timestamp(2020, 1, 31)
    date_max = pd.Timestamp(2020, 3, 1)

    # Left joins products and orders to keep all products
    merged = products.merge(orders, on="product_id", how="left")
    # Filters orders made in february
    output = merged[(merged["order_date"] > date_min) & (merged["order_date"] < date_max)]
    # Transforms units to be the units sum groupped by product_id
    output["unit"] = output.groupby("product_id")["unit"].transform("sum")
    # Filters products with more than or equal 100 units and drops duplicates
    output = output[output["unit"] >= 100].drop_duplicates("product_id")

    # Returns the desired columns
    return output[["product_name", "unit"]]
