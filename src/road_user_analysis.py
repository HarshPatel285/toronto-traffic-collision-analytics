import pandas as pd

def pedestrian_collisions(df: pd.DataFrame) -> int:
    """
    Count collisions involving pedestrians.
    """
    if "PEDESTRIAN" not in df.columns:
        raise ValueError("Dataset must contain PEDESTRIAN column")

    return len(df[df["PEDESTRIAN"] == "YES"])