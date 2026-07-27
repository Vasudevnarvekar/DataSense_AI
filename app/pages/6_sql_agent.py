import os
import sys
import time
import streamlit as st

# ---------------------------------------------------
# Add Project Root to Python Path
# ---------------------------------------------------

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from utils.sql_engine import (
    create_database,
    execute_query
)

# ---------------------------------------------------
# Page Title
# ---------------------------------------------------

st.title("🗄️ SQL Agent")

# ---------------------------------------------------
# Check Dataset
# ---------------------------------------------------

if "cleaned_df" not in st.session_state:
    st.warning("Please upload and clean a dataset first.")
    st.stop()

df = st.session_state["cleaned_df"]

# ---------------------------------------------------
# Dataset Information
# ---------------------------------------------------

st.subheader("📋 Dataset Information")

col1, col2 = st.columns(2)

with col1:
    st.info("**Table Name:** dataset")

with col2:
    st.info(f"**Total Columns:** {len(df.columns)}")

st.write("### Available Columns")
st.write(", ".join(df.columns))

# ---------------------------------------------------
# Query History
# ---------------------------------------------------

if "query_history" not in st.session_state:
    st.session_state.query_history = []

# ---------------------------------------------------
# Create SQLite Database
# ---------------------------------------------------

conn = create_database(df)

# ---------------------------------------------------
# Sample SQL Queries
# ---------------------------------------------------

sample_queries = {
    "Show First 10 Rows":
        "SELECT * FROM dataset LIMIT 10;",

    "Count Total Rows":
        "SELECT COUNT(*) AS Total_Rows FROM dataset;",

    "Show All Columns":
        "SELECT * FROM dataset;",

    "Show Distinct Values":
        "SELECT DISTINCT * FROM dataset LIMIT 10;"
}

selected_query = st.selectbox(
    "Choose a Sample Query",
    list(sample_queries.keys())
)

# ---------------------------------------------------
# SQL Editor
# ---------------------------------------------------

query = st.text_area(
    "Enter SQL Query",
    value=sample_queries[selected_query],
    height=180
)

# ---------------------------------------------------
# Run Query
# ---------------------------------------------------

if st.button("▶ Run Query"):

    try:

        start_time = time.perf_counter()

        result = execute_query(conn, query)

        execution_time = time.perf_counter() - start_time

        # Save query in history
        if query not in st.session_state.query_history:
            st.session_state.query_history.insert(0, query)

        st.success("✅ Query Executed Successfully!")

        st.caption(f"⏱ Execution Time: {execution_time:.6f} seconds")

        st.dataframe(result, use_container_width=True)

        # ---------------------------------------------
        # Download Results
        # ---------------------------------------------

        csv = result.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇ Download Results as CSV",
            data=csv,
            file_name="sql_results.csv",
            mime="text/csv"
        )

    except Exception as e:

        st.error(f"❌ SQL Error: {e}")

# ---------------------------------------------------
# Query History
# ---------------------------------------------------

if st.session_state.query_history:

    with st.expander("🕒 Query History"):

        for i, q in enumerate(st.session_state.query_history, start=1):

            st.code(q, language="sql")

# ---------------------------------------------------
# SQL Cheat Sheet
# ---------------------------------------------------

with st.expander("💡 SQL Cheat Sheet"):

    st.markdown("""
### Basic SQL Queries

**Show all rows**

```sql
SELECT * FROM dataset;
```

**Show first 10 rows**

```sql
SELECT * FROM dataset
LIMIT 10;
```

**Count total rows**

```sql
SELECT COUNT(*)
FROM dataset;
```

**Unique values**

```sql
SELECT DISTINCT column_name
FROM dataset;
```

**Average value**

```sql
SELECT AVG(column_name)
FROM dataset;
```

**Maximum value**

```sql
SELECT MAX(column_name)
FROM dataset;
```

**Minimum value**

```sql
SELECT MIN(column_name)
FROM dataset;
```

**Group By**

```sql
SELECT column_name, COUNT(*)
FROM dataset
GROUP BY column_name;
```

**Filter rows**

```sql
SELECT *
FROM dataset
WHERE column_name > 100;
```

**Sort data**

```sql
SELECT *
FROM dataset
ORDER BY column_name DESC;
```
""")