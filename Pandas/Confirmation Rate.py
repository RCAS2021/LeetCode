import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    # Left join signups and confirmations on user_id
    output = signups.merge(confirmations, on="user_id", how="left")
    # Gets total action count groupped by user_id
    total = output.groupby("user_id").count().reset_index()[["user_id", "action"]]
    # Gets total confirmed action count groupped by user_id
    confirm = output[output["action"] == "confirmed"].groupby("user_id").count().reset_index()[["user_id", "action"]]
    # Left join total and confirm on user_id
    output = total.merge(confirm, on="user_id", how="left")
    # Creates column confirmation rate, receiving rounded value between action_y(confirmed) / action_x(total) to 2 decimal places
    output["confirmation_rate"] = round(output["action_y"]/output["action_x"], 2)
    # Returns user_id and confirmation_rate from output, filling nan values with 0
    return output[["user_id", "confirmation_rate"]].fillna(0)
