from src.data_loader import load_dataset
from src.data_cleaning import clean_dataset


def test_clean_dataset():

    df = load_dataset("data/Traffic_Collisions_Open_Data.csv")

    clean_df = clean_dataset(df)

    assert clean_df is not None
    assert len(clean_df) > 0
