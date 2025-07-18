import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    # Use vectorized replace to swap 'm' and 'f'
    salary['sex'] = salary['sex'].replace({'m': 'f', 'f': 'm'})
    return salary
