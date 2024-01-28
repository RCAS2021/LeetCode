import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    scores = scores.sort_values(by='rank')
    return scores[['score', 'rank']]

# rank -> https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rank.html