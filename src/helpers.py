import pandas as pd

def memory_report(df: pd.DataFrame):
    mem = df.memory_usage(deep=True).sum() / (1024**2)
    return f"DataFrame uses {mem:.2f} MB"
