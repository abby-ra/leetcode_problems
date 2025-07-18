import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    # Merge sales and product tables on product_id
    merged = pd.merge(sales, product, on='product_id')
    
    # Select required columns
    result = merged[['product_name', 'year', 'price']]
    
    return result
