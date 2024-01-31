import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    output = daily_sales.groupby(['date_id', 'make_name'])[['lead_id', 'partner_id']].nunique().reset_index()
    output.columns = ['date_id', 'make_name', 'unique_leads', 'unique_partners']
    return output

# Using agg
import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    output = daily_sales.groupby(['date_id', 'make_name']).agg({'lead_id': 'nunique', 'partner_id': 'nunique'}).reset_index()
    output.columns = ['date_id', 'make_name', 'unique_leads', 'unique_partners']
    return output