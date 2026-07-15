import pandas as pd


def load_file(uploaded_file):
    """
    Load CSV or Excel file into a Pandas DataFrame.

    Parameters
    ----------
    uploaded_file : UploadedFile
        File uploaded through Streamlit.

    Returns
    -------
    pandas.DataFrame
    """

    filename = uploaded_file.name.lower()

    if filename.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    elif filename.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)

    else:
        raise ValueError("Unsupported file format.")

    return df