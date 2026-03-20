from src.data_loader import load_dataset
from src.data_cleaning import clean_dataset
from src.road_user_analysis import pedestrian_collisions, bicycle_collisions, motorcycle_collisions, automobile_collisions


def test_pedestrian_collisions():

    df = load_dataset("data/Traffic_Collisions_Open_Data.csv")
    df = clean_dataset(df)

    result = pedestrian_collisions(df)

    assert result >= 0
