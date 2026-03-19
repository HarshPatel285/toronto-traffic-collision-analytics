import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd

from src.data_loader import load_dataset
from src.data_cleaning import clean_dataset

from src.time_analysis import (
    collisions_by_hour,
    collisions_by_weekday,
    collisions_by_month,
    peak_collision_hour,
    peak_collision_day
)

from src.location_analysis import (
    top_neighbourhoods,
    most_dangerous_neighbourhood
)

from src.road_user_analysis import (
    vulnerable_road_user_summary,
    most_vulnerable_user
)

from src.severity_analysis import (
    severity_distribution,
    most_common_severity
)


# ------------------------------------------------
# Page Configuration
# ------------------------------------------------

st.set_page_config(
    page_title="Toronto Traffic Collision Analytics (Group 7)",
    page_icon="🚗",
    layout="wide"
)

# ------------------------------------------------
# Load Data
# ------------------------------------------------

@st.cache_data
def load_data():

    df = load_dataset("data/Traffic_Collisions_Open_Data.csv")

    df = clean_dataset(df)

    return df


df = load_data()

# ------------------------------------------------
# Sidebar Filters
# ------------------------------------------------

st.sidebar.header("Dashboard Filters")

neighbourhoods = sorted(df["NEIGHBOURHOOD_158"].dropna().unique())

selected_neighbourhood = st.sidebar.selectbox(
    "Select Neighbourhood",
    ["All"] + neighbourhoods
)

if selected_neighbourhood != "All":
    df = df[df["NEIGHBOURHOOD_158"] == selected_neighbourhood]


# ------------------------------------------------
# Dashboard Title
# ------------------------------------------------

st.title("🚗 Toronto Traffic Collision Analytics Dashboard (Group 7)")

st.write(
"""
Interactive analytics tool exploring **Toronto traffic collision patterns**
using data analysis and visualization.
"""
)