import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    report = report.melt(id_vars='product', var_name='quarter', value_name='sales')
    return report

# melt -> https://pandas.pydata.org/docs/user_guide/reshaping.html#melt-and-wide-to-long