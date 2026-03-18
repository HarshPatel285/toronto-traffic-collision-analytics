import pandas as pd

def pedestrian_collisions(df: pd.DataFrame) -> int:
    """
    Count collisions involving pedestrians.
    """
    if "PEDESTRIAN" not in df.columns:
        raise ValueError("Dataset must contain PEDESTRIAN column")

    return len(df[df["PEDESTRIAN"] == "YES"])


def motorcycle_collisions(df: pd.DataFrame) -> int:
    """
    Count collisions involving motorcycles.
    """
    if "MOTORCYCLE" not in df.columns:
        raise ValueError("Dataset must contain MOTORCYCLE column")

    return len(df[df["MOTORCYCLE"] == "YES"])


def bicycle_collisions(df: pd.DataFrame) -> int:
    """
    Count collisions involving bicycles.
    """
    if "BICYCLE" not in df.columns:
        raise ValueError("Dataset must contain BICYCLE column")

    return len(df[df["BICYCLE"] == "YES"])


def automobile_collisions(df: pd.DataFrame) -> int:
    """
    Count collisions involving automobiles.
    """
    if "AUTOMOBILE" not in df.columns:
        raise ValueError("Dataset must contain AUTOMOBILE column")

    return len(df[df["AUTOMOBILE"] == "YES"])


def vulnerable_road_user_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate summary table for vulnerable road users.
    """

    pedestrian = pedestrian_collisions(df)
    bicycle = bicycle_collisions(df)
    motorcycle = motorcycle_collisions(df)
    automobile = automobile_collisions(df)

    summary = pd.DataFrame({
        "Road_User_Type": [
            "Pedestrian",
            "Bicycle",
            "Motorcycle",
            "Automobile"
        ],
        "Collision_Count": [
            pedestrian,
            bicycle,
            motorcycle,
            automobile
        ]
    })

    return summary


def most_vulnerable_user(df: pd.DataFrame) -> str:
    """
    Identify the most vulnerable road user group.
    """

    summary = vulnerable_road_user_summary(df)

    return summary.loc[
        summary["Collision_Count"].idxmax(),
        "Road_User_Type"
    ]
