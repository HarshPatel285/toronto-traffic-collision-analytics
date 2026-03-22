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

def collision_point_map(df: pd.DataFrame):
    """
    Generate interactive collision point map.
    """

    map_df = prepare_map_data(df)

    # sample data to improve performance
    map_df = map_df.sample(min(len(map_df), 5000))

    fig = px.scatter_mapbox(
        map_df,
        lat="LAT_WGS84",
        lon="LONG_WGS84",
        zoom=10,
        height=500
    )

    fig.update_layout(mapbox_style="open-street-map")

    return fig

def collision_density_map(df: pd.DataFrame):
    """
    Generate collision density heatmap.
    """

    map_df = prepare_map_data(df)

    # sample data for performance
    map_df = map_df.sample(min(len(map_df), 10000))

    fig = px.density_mapbox(
        map_df,
        lat="LAT_WGS84",
        lon="LONG_WGS84",
        radius=8,
        zoom=10,
        height=600
    )

    fig.update_layout(mapbox_style="open-street-map")

    return fig