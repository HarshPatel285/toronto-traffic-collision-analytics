from src.data_loader import load_dataset
from src.map_visualization import prepare_map_data

# 16 >> US-14
def test_prepare_map_data():

    df = load_dataset("data/Traffic_Collisions_Open_Data.csv")

    result = prepare_map_data(df)

    assert result is not None
    assert len(result) > 0