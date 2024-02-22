import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    # Gets only the rows where activity_date is in between 27-06-2019 and 27-07-2019 (included)
    filtered = activity[
        (activity["activity_date"] > pd.Timestamp('2019-06-27')) 
        &
        (activity["activity_date"] <= pd.Timestamp('2019-07-27'))
    ]

    # Groups by activity_date and counts unique user_ids,
    # then resets index and renames to active_users
    active_users = filtered.groupby("activity_date")["user_id"].nunique().reset_index(name="active_users")

    # Rename activity_date to day
    output = active_users.rename(columns={"activity_date": "day"})

    return output
