import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    all_orders = sales_person.merge(orders, on='sales_id', how='left').merge(company, on='com_id', how='left')
    no_orders = all_orders[(all_orders['name_y'] != 'RED') | (all_orders['name_y'].isna())]
    has_orders = all_orders[all_orders['name_y'] == 'RED']['name_x'].unique()
    output = no_orders[['name_x']].rename(columns={'name_x': 'name'})
    output = output.drop_duplicates()
    output = output[~output['name'].isin(has_orders)]

    return output