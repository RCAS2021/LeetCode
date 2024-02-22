import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    # Left join users and register on user_id
    output = users.merge(register, on="user_id", how="left")
    # Calculates total unique user_id quantity
    total = output["user_id"].nunique()
    # Groups by contest_id, aggregating user_count = unique user_ids and resets index
    output = output.groupby("contest_id").agg(user_count=('user_id', 'nunique')).reset_index()
    # Assigns percentage to be the rounded average (user_count by contest_id divided by total number of user_ids), multiplied by 100 (percentage) by 2 decimal places 
    output = output.assign(
        percentage=lambda i: round((i.user_count / total) * 100, 2)
    )
    # Returns contest_id, percentage, sorted by percentage DESC, if there is a tie, contest_id ASC
    return output[["contest_id", "percentage"]].sort_values(["percentage", "contest_id"], ascending=[False, True])
