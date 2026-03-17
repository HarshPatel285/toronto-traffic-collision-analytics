from src.data_loader import load_dataset
from src.data_cleaning import clean_dataset
from src.location_analysis import collisions_by_neighbourhood

def test_collisions_by_neighbourhood():

    df = load_dataset("data/Traffic_Collisions_Open_Data.csv")

    df = clean_dataset(df)

    result = collisions_by_neighbourhood(df)

    assert result is not None
    assert len(result) > 0