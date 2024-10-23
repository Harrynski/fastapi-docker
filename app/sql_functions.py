import pandas as pd
import sqlite3

def run_query(script: str, path_to_data_base: str) -> pd.DataFrame:
    conn = sqlite3.connect(path_to_data_base)
    cursor = conn.cursor()
    cursor.executescript(script)
    conn.commit()
    conn.close()
    return script

def run_query_to_dataframe(query: str, path_to_data_base: str) -> pd.DataFrame:
    conn = sqlite3.connect(path_to_data_base)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df