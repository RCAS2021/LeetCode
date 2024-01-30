import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.groupby('customer_number')['order_number'].count().reset_index()
    orders = orders.loc[orders['order_number'] == orders['order_number'].max(), ['customer_number']]
    return orders

# Using Mode
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return orders['customer_number'].mode().to_frame()

# mode -> https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mode.html
# to_frame -> https://pandas.pydata.org/docs/reference/api/pandas.Series.to_frame.html