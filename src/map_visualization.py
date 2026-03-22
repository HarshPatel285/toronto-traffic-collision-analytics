import pandas as pd
import plotly.express as px

def prepare_map_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare dataset for map visualization.

    Removes rows with invalid coordinates.
    """

    required_columns = ["LAT_WGS84", "LONG_WGS84"]

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Dataset must contain {col}")

    map_df = df[["LAT_WGS84", "LONG_WGS84"]].dropna()

    # remove invalid coordinates
    map_df = map_df[
        (map_df["LAT_WGS84"] != 0) &
        (map_df["LONG_WGS84"] != 0)
    ]

    return map_df