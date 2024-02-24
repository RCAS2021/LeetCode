import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    # Using iterrows, gets row index and row
    for index, row in triangle.iterrows():
        # if x + y > z and x + z > y and z + y > x
        if (row.x + row.y > row.z) & (row.x + row.z > row.y) & (row.z + row.y > row.x):
            # Finds the index on the triangle dataframe and sets the column triangle to Yes
            triangle.loc[index, "triangle"] = "Yes"
        else:
            # Finds the index on the triangle dataframe and sets the column triangle to No
            triangle.loc[index, "triangle"] = "No"

    return triangle


# Iterrows() -> https://www.freecodecamp.org/news/how-to-iterate-over-rows-with-pandas-loop-through-a-dataframe/

# Loc -> https://saturncloud.io/blog/how-to-update-values-in-a-specific-row-in-a-python-pandas-dataframe/
# import pandas as pd

# create a sample DataFrame
# df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# update the values in the second row, columns A and C
# df.iloc[1, [0, 2]] = [10, 30]
# 

# print(df)