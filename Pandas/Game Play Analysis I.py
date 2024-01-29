import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.sort_values(by='event_date')
    activity['first_login'] = activity.groupby('player_id')['event_date'].head(1)
    output = pd.DataFrame({'player_id': activity['player_id'], 'first_login': activity['first_login']}).dropna()
    return output