import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    # To use diff, sorting is needed
    activity = activity.sort_values(['machine_id', 'process_id', 'timestamp'])
    # Groups by machine_id, process_id and takes the diff in timestamps
    activity['diff'] = activity.groupby(['machine_id', 'process_id'])['timestamp'].diff()
    # Drops nan diffs
    activity = activity.dropna(subset=['diff'])
    # Returns rounded avg diffs groupped by machine_id and renamed
    return activity.groupby('machine_id')['diff'].mean().round(3).reset_index(name="processing_time")
