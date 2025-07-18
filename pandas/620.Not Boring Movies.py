import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    # Filter for odd ids and non-boring descriptions
    filtered = cinema[(cinema['id'] % 2 == 1) & (cinema['description'] != 'boring')]

    # Sort by rating descending
    result = filtered.sort_values(by='rating', ascending=False)

    return result
