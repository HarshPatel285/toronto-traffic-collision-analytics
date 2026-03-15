import pandas as pd


def collisions_by_neighbourhood(df: pd.DataFrame) -> pd.Series:
    """
    Calculate number of collisions by neighbourhood.
    """

    if "NEIGHBOURHOOD_158" not in df.columns:
        raise ValueError("Dataset must contain NEIGHBOURHOOD_158 column")

    neighbourhood_counts = df.groupby("NEIGHBOURHOOD_158").size()

    return neighbourhood_counts.sort_values(ascending=False)


def top_neighbourhoods(df: pd.DataFrame, top_n: int = 10) -> pd.Series:
    """
    Return top N neighbourhoods with highest collision counts.
    """

    counts = collisions_by_neighbourhood(df)

    return counts.head(top_n)


def collision_percentage_by_neighbourhood(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate percentage share of collisions by neighbourhood.
    """

    counts = collisions_by_neighbourhood(df)

    total = counts.sum()

    percentages = (counts / total) * 100

    result = pd.DataFrame({
        "Neighbourhood": percentages.index,
        "Collision_Percentage": percentages.values
    })

    return result


def neighbourhood_collision_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create summary table for neighbourhood collisions.
    """

    counts = collisions_by_neighbourhood(df)

    summary = counts.reset_index()

    summary.columns = ["Neighbourhood", "Collisions"]

    return summary


def most_dangerous_neighbourhood(df: pd.DataFrame) -> str:
    """
    Identify neighbourhood with highest collision count.
    """

    counts = collisions_by_neighbourhood(df)

    return counts.idxmax()