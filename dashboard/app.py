import sys
import os

from src.map_visualization import collision_point_map, collision_density_map

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

# ------------------------------------------------
# KPI Metrics
# ------------------------------------------------

st.header("Key Collision Metrics")

col1, col2, col3, col4 = st.columns(4)

total_collisions = len(df)
fatalities = df["FATALITIES"].sum()
injury_collisions = len(df[df["INJURY_COLLISIONS"] == "YES"])
pedestrian_collisions = len(df[df["PEDESTRIAN"] == "YES"])

col1.metric("Total Collisions", total_collisions)
col2.metric("Fatalities", fatalities)
col3.metric("Injury Collisions", injury_collisions)
col4.metric("Pedestrian Collisions", pedestrian_collisions)

# ------------------------------------------------
# Dashboard Tabs
# ------------------------------------------------

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Time Analysis",
    "Location Analysis",
    "Road User Safety",
    "Collision Maps",
    "Dataset Viewer"
])

# ------------------------------------------------
# Time Analysis
# ------------------------------------------------

with tab1:

    st.header("Collision Trends Over Time")

    option = st.selectbox(
        "Select Time Analysis",
        ["Hour", "Weekday", "Month"]
    )

    if option == "Hour":

        hourly_data = collisions_by_hour(df)

        st.bar_chart(hourly_data)

    elif option == "Weekday":

        weekday_data = collisions_by_weekday(df)

        st.bar_chart(weekday_data)

    else:

        monthly_data = collisions_by_month(df)

        st.line_chart(monthly_data)

# ------------------------------------------------
# Location Analysis
# ------------------------------------------------

with tab2:

    st.header("Top Collision Neighbourhoods")

    top_locations = top_neighbourhoods(df)

    st.bar_chart(top_locations)

    st.dataframe(top_locations)

# ------------------------------------------------
# Road User Safety Analysis
# ------------------------------------------------

with tab3:

    st.header("Vulnerable Road User Analysis")

    road_user_data = vulnerable_road_user_summary(df)

    st.dataframe(road_user_data)

    st.bar_chart(road_user_data.set_index("Road_User_Type"))

# ------------------------------------------------
# Collision Map Visualization
# ------------------------------------------------

with tab4:

    st.header("Collision Location Map")

    fig = collision_point_map(df)

    st.plotly_chart(fig, use_container_width=True)

    st.header("Collision Density Heatmap")

    density_fig = collision_density_map(df)

    st.plotly_chart(density_fig, use_container_width=True)
# ------------------------------------------------
# Dataset Viewer
# ------------------------------------------------

with tab5:

    st.header("Dataset Preview")

    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])

    st.dataframe(df.head(100))

# ------------------------------------------------
# Automated Insights
# ------------------------------------------------

st.markdown("---")

st.header("Automated Insights")

peak_hour = peak_collision_hour(df)
peak_day = peak_collision_day(df)
danger_area = most_dangerous_neighbourhood(df)
vulnerable_user = most_vulnerable_user(df)
common_severity = most_common_severity(df)

st.success(f"Peak collision hour: {peak_hour}:00")
st.warning(f"Most dangerous weekday: {peak_day}")
st.error(f"Neighbourhood with most collisions: {danger_area}")

st.info(f"Most vulnerable road user group: {vulnerable_user}")
st.info(f"Most common collision severity: {common_severity}")

# ------------------------------------------------
# Footer
# ------------------------------------------------

st.markdown("---")

st.write("Toronto Traffic Collision Analytics Tool")
st.write("Built with Python, Pandas, Streamlit, and Plotly")