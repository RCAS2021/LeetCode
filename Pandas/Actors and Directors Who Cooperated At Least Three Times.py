import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    output = actor_director.groupby(['actor_id', 'director_id']).agg('count').reset_index()
    output = output.loc[output['timestamp'] > 2, ['actor_id', 'director_id']]
    return output