import sqlite3
import pandas as pd


def create_database(df, table_name="dataset"):
    """
    Creates an in-memory SQLite database
    and stores the dataframe as a table.
    """

    conn = sqlite3.connect(":memory:")

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    return conn


def execute_query(conn, query):
    """
    Executes SQL query and returns the result
    as a Pandas DataFrame.
    """

    result = pd.read_sql_query(query, conn)

    return result