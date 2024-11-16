import pandas as pd

# Load blacklist from CSV
def load_blacklist():
    try:
        blacklist_df = pd.read_csv("blacklist.csv")
        return set(blacklist_df["url"].tolist())
    except FileNotFoundError:
        return set()

# Check if a URL is in the blacklist
def is_blacklisted(url, blacklist):
    return any(site in url for site in blacklist)
