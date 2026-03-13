from src.data_loader import load_dataset
import pandas as pd


def test_load_dataset_success():

    df = load_dataset("data/Traffic_Collisions_Open_Data.csv")

    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_load_dataset_file_not_found():

    try:
        load_dataset("data/non_existing_file.csv")
    except FileNotFoundError:
        assert True