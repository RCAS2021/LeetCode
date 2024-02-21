import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    # Filters if id is odd and description isn't boring
    output = cinema[(cinema["id"] % 2 != 0) & (cinema["description"] != "boring")]
    # Sort by rating descending
    output = output.sort_values("rating", ascending=False)

    return output
