from src.data_loader import load_dataset
from src.data_cleaning import clean_dataset
from src.time_analysis import collisions_by_hour


def test_collisions_by_hour():

    df = load_dataset("data/Traffic_Collisions_Open_Data.csv")

    df = clean_dataset(df)

    result = collisions_by_hour(df)

    assert result is not None
    assert len(result) > 0