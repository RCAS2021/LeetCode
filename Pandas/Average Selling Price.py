import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    # Left join prices and units_sold on product_id, assigning total_price = row.price * row.units and purchase_date if null = row.start_date else row.purchase_date
    output = prices.merge(units_sold, on="product_id", how="left").assign(
        total_price=lambda i: i.price * i.units,
        purchase_date=lambda i: i.apply(lambda r: r.start_date if pd.isnull(r.purchase_date) else r.purchase_date, axis=1)
    )
    # Fills NaN values with 0
    output = output.fillna(0)
    # Queries row with purchase date between start_date and end_date
    output = output.query("start_date <= purchase_date <= end_date")
    # Groups by product_id, aggregating the sum of total_prices and sum of units, then assigns average_price to be the rounded average by 2 decimal places and resets index
    output = output.groupby("product_id").agg({"total_price": "sum", "units": "sum"}).assign(
        average_price=lambda i: round(i.total_price / i.units, 2)
    )[["average_price"]].reset_index()
    # Fills NaN values with 0
    output = output.fillna(0, axis=1)
    return output
