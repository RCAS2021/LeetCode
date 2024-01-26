import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    res = customers.merge(orders, left_on='id', right_on='customerId', how='outer', suffixes=('_customers', '_orders'))
    res = res.loc[res['customerId'].isna(), ['name']].rename(columns={'name': 'Customers'})
    return res