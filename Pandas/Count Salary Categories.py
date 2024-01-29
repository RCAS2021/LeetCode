import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_salary = accounts.loc[accounts['income'] < 20000].count()
    average_salary = accounts.loc[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)].count()
    high_salary = accounts.loc[accounts['income'] > 50000].count()
    accounts = pd.DataFrame({'category': ['High Salary', 'Low Salary', 'Average Salary'], 'accounts_count': [high_salary[0], low_salary[0], average_salary[0]]})
    return accounts