import pandas as pd


def load_file(uploaded_file):
    filename = uploaded_file.name.lower()

    try:
        if filename.endswith(".csv"):
            try:
                # Standard CSV
                df = pd.read_csv(uploaded_file)
            except Exception:
                # Retry with Python engine
                uploaded_file.seek(0)
                df = pd.read_csv(uploaded_file, engine="python")

        elif filename.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)

        else:
            raise ValueError("Unsupported file format.")

        return df

    except Exception as e:
        raise ValueError(f"Error loading file: {e}")