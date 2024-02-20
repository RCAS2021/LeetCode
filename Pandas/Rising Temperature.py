import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values("recordDate")
    output = weather[
        # Checks temperature difference in previous row
        (weather["temperature"].diff() > 0 )
          &
        # Checks if the difference between recorded dates is 1 day (Guarantees previous day instead of previous date)
        (weather["recordDate"].diff() == "1 days")
        ]
    return output[["id"]]

# Diff -> https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.diff.html
