import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    output = my_numbers["num"].drop_duplicates(keep=False)

    return pd.DataFrame({"num": [max(output, default = None)]})
