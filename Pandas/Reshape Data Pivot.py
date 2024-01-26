import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.pivot(index='month', columns='city', values='temperature')
    return weather

# pivot -> https://pandas.pydata.org/docs/user_guide/reshaping.html#pivot