import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    animals = animals.sort_values(by='weight', ascending=False).loc[animals['weight'] > 100, ['name']]
    return animals