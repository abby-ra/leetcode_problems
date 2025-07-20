import pandas as pd

def valid_emails(Users: pd.DataFrame) -> pd.DataFrame:
    # Regex pattern: starts with a letter, followed by allowed characters, ends with @leetcode.com
    pattern = r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$'
    
    # Filter valid emails using the pattern
    return Users[Users['mail'].str.match(pattern)]
