def load_price_data(path):
    df = pd.read_csv(path)

    # normalize date column
    if "Date" not in df.columns:
        if "Unnamed: 0" in df.columns:
            df = df.rename(columns={"Unnamed: 0": "Date"})
        elif "Datetime" in df.columns:
            df = df.rename(columns={"Datetime": "Date"})
        else:
            raise KeyError(f"No Date-like column found. Columns: {list(df.columns)}")

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # drop formatting artifacts
    df = (
        df.dropna(subset=["Date"])
          .sort_values("Date")
          .reset_index(drop=True)
    )

    return df
