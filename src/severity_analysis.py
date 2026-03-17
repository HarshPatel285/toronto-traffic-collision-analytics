import pandas as pd

def fatal_collisions(df: pd.DataFrame) -> int:
    """
    Count fatal collisions.
    """

    if "FATALITIES" not in df.columns:
        raise ValueError("Dataset must contain FATALITIES column")

    return len(df[df["FATALITIES"] > 0])

def injury_collisions(df: pd.DataFrame) -> int:
    """
    Count injury collisions.
    """

    if "INJURY_COLLISIONS" not in df.columns:
        raise ValueError("Dataset must contain INJURY_COLLISIONS column")

    return len(df[df["INJURY_COLLISIONS"] == "YES"])


def property_damage_collisions(df: pd.DataFrame) -> int:
    """
    Count property damage collisions.
    """

    if "PD_COLLISIONS" not in df.columns:
        raise ValueError("Dataset must contain PD_COLLISIONS column")

    return len(df[df["PD_COLLISIONS"] == "YES"])

def fatal_collision_flag(df: pd.DataFrame) -> int:
    """
    Count collisions flagged as fatal.
    """

    if "FTR_COLLISIONS" not in df.columns:
        raise ValueError("Dataset must contain FTR_COLLISIONS column")

    return len(df[df["FTR_COLLISIONS"] == "YES"])

def severity_distribution(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate severity distribution table.
    """

    fatal = fatal_collisions(df)
    injury = injury_collisions(df)
    property_damage = property_damage_collisions(df)

    severity_df = pd.DataFrame({
        "Severity_Type": [
            "Fatal Collisions",
            "Injury Collisions",
            "Property Damage Collisions"
        ],
        "Collision_Count": [
            fatal,
            injury,
            property_damage
        ]
    })

    return severity_df

def most_common_severity(df: pd.DataFrame) -> str:
    """
    Identify most common collision severity.
    """

    severity_df = severity_distribution(df)

    return severity_df.loc[
        severity_df["Collision_Count"].idxmax(),
        "Severity_Type"
    ]