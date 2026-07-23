import pandas as pd


def load_file(uploaded_file):
    filename = uploaded_file.name.lower()

    try:
        if filename.endswith(".csv"):

            # Common encodings to try
            encodings = ["utf-8", "utf-8-sig", "latin1", "cp1252"]

            for encoding in encodings:
                try:
                    uploaded_file.seek(0)
                    return pd.read_csv(uploaded_file, encoding=encoding)
                except UnicodeDecodeError:
                    continue
                except Exception:
                    uploaded_file.seek(0)
                    try:
                        return pd.read_csv(
                            uploaded_file,
                            encoding=encoding,
                            engine="python"
                        )
                    except Exception:
                        continue

            raise ValueError(
                "Unable to read the CSV file. Please check its encoding or format."
            )

        elif filename.endswith((".xlsx", ".xls")):
            return pd.read_excel(uploaded_file)

        else:
            raise ValueError("Unsupported file format. Please upload a CSV or Excel file.")

    except Exception as e:
        raise ValueError(f"Error loading file: {e}")