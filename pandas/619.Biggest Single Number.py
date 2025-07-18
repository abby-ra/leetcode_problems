import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    # Count occurrences of each number
    counts = my_numbers['num'].value_counts()

    # Filter numbers that appeared only once
    single_numbers = counts[counts == 1].index

    if not single_numbers.empty:
        result = pd.DataFrame({'num': [max(single_numbers)]})
    else:
        result = pd.DataFrame({'num': [None]})

    return result
