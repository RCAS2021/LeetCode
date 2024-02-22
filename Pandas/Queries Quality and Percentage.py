import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    # Assign quality to be the rating / position + 1e-6 (small positive constant, equivalent to 0.000001, prevents errors)
    output = queries.assign(
        quality=lambda i: i.rating / i.position + 1e-6
    )

    # Groupys by query_name and aggregates query_total to be the rating count and resets index
    total = output.groupby("query_name").agg(query_total=('rating', 'count')).reset_index()

    # Gets rows with rating < 3
    poor = output[output["rating"] < 3]
    # Groups by query_name and gets the count of poor queries
    poor = output[output["rating"] < 3].groupby("query_name").size().reset_index(name="cnt")
    # Right joins with total, to get all possible query_names, then fills NaN values with 0
    poor = poor.merge(total, on="query_name", how="right").fillna(0)
    
    # Groups by query_name, aggregates quality to its mean, resets index,
    # then assigns poor_query_percentage to be the poor queries count divided by total queries count,
    # and multiplies the division by 100
    output = output.groupby("query_name").agg({"quality": "mean"}).reset_index().assign(
        poor_query_percentage=lambda i: (poor.cnt / poor.query_total) * 100
    )

    # Returns output rounded by 2 decimal places
    return output.round(2)


# Remaking

import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    output = queries
    # Quality = rating/position + 1e-6 (small positive constant, equivalent to 0.000001, prevents errors)
    output['quality'] = output.rating/output.position + 1e-6
    # Poor_query_percentage = output.rating < 3 * 100
    output['poor_query_percentage'] = (output.rating < 3) * 100
    # Groups by query_name, aggregating the averages of quality and poor_query_percentage, rounding to 2 decimal places and resets the index
    output = output.groupby('query_name').agg({'quality': 'mean', 'poor_query_percentage': 'mean'}).round(2).reset_index()
    return output
