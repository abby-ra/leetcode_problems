import pandas as pd

def find_customers(Visits: pd.DataFrame, Transactions: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Left join Visits with Transactions on visit_id
    merged = Visits.merge(Transactions, on='visit_id', how='left')

    # Step 2: Filter visits with no transactions (transaction_id is NaN)
    no_trans = merged[merged['transaction_id'].isna()]

    # Step 3: Group by customer_id and count those visits
    result = no_trans.groupby('customer_id').size().reset_index(name='count_no_trans')

    return result
