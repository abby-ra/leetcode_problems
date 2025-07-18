import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # Group by actor_id and director_id, and count cooperations
    grouped = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='count')
    
    # Filter pairs with at least 3 cooperations
    result = grouped[grouped['count'] >= 3][['actor_id', 'director_id']]

    return result
