from src.data_loader import load_dataset
from src.data_cleaning import clean_dataset
from src.severity_analysis import fatal_collisions

# 6 >> US-6
def test_fatal_collisions():

    df = load_dataset("data/Traffic_Collisions_Open_Data.csv")
    df = clean_dataset(df)

    result = fatal_collisions(df)

    assert result >= 0