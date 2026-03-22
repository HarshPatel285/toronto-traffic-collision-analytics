# 🚗 Toronto Traffic Collision Analytics Dashboard (Group 7)

## 📌 Project Overview
This project is an interactive data analytics system designed to analyze traffic collision data in Toronto.  
It provides insights into collision patterns using data processing, analysis, and visualization techniques.

The system was developed using Agile (Scrum) methodology, with iterative implementation of user stories across multiple sprints.

---

## 🎯 Objectives
- Analyze traffic collision trends  
- Identify high-risk time periods and locations  
- Evaluate road user safety (pedestrians, cyclists, etc.)  
- Understand collision severity patterns  
- Provide an interactive dashboard for data exploration  

---

## 🧠 Key Features

### 📊 Data Processing
- Dataset loading and validation  
- Data cleaning pipeline  
- Handling missing values and invalid records  

### ⏱️ Time Analysis
- Collisions by hour  
- Collisions by weekday  
- Monthly collision trends  
- Peak collision time detection  

### 📍 Location Analysis
- Collisions by neighbourhood  
- High-risk area identification  

### 🚶 Road User Safety
- Pedestrian collision analysis  
- Cyclist collision analysis  
- Motorcycle and automobile involvement  
- Vulnerable road user identification  

### ⚠️ Severity Analysis
- Fatal collisions  
- Injury collisions  
- Property damage collisions  
- Severity distribution insights  

### 🖥️ Dashboard
- Built with Streamlit  
- Interactive filters  
- KPI metrics  
- Multi-tab layout  
- Automated insights  

### 🧪 Testing
- Unit tests using pytest  
- Validation of analytics functions  

---

## 🏗️ Project Structure

traffic-collision-analytics/

│  
├── data/  
│   Traffic_Collisions_Open_Data.csv  
│  
├── src/  
│   data_loader.py  
│   data_cleaning.py  
│   time_analysis.py  
│   location_analysis.py  
│   road_user_analysis.py  
│   severity_analysis.py  
│   map_visualization.py  
│   utils.py  
│  
├── dashboard/  
│   app.py  
│  
├── tests/  
│   test_data_loader.py  
│   test_data_cleaning.py  
│   test_time_analysis.py  
│   test_location_analysis.py  
│   test_road_user_analysis.py  
│   test_severity_analysis.py  
│  
├── requirements.txt  
├── README.md  
└── .gitignore  

---

## ⚙️ Installation

### 1. Clone Repository
git clone <your-repo-link>  
cd toronto-traffic-collision-analytics  

### 2. Install Dependencies
pip install -r requirements.txt  

---

## ▶️ Run the Application

streamlit run dashboard/app.py  

The dashboard will open in your browser.

---

## 🧪 Run Tests

pytest  

---

## 📊 Sample Insights
- Peak collision hours occur during evening rush hours  
- Certain neighbourhoods show consistently higher collision rates  
- Pedestrians and cyclists are among the most vulnerable road users  
- Most collisions result in property damage rather than fatalities  

---

## 🔄 Agile Methodology

This project followed the Scrum Agile framework:

### 📌 Product Backlog
User stories defining system features  

### 🚀 Sprints
- Sprint 1: Data loading, cleaning, and time analysis  
- Sprint 2: Location and road user analysis  
- Sprint 3: Dashboard, visualization, and testing  

### 🛠 Tools Used
- Taiga (project management)  
- GitHub (version control)  
- Pull Requests (code review)
- Pycharm (coding)

---

## 👥 Team
Group 7  

---

## 🧾 Technologies Used
- Python  
- Pandas  
- Streamlit  
- Plotly  
- Pytest  

---

## ✅ Project Status
✔ Completed  
✔ Fully functional  
✔ Ready for demonstration  

---

## 📌 Conclusion
This project demonstrates a complete data analytics pipeline, from data ingestion and cleaning to analysis and interactive visualization.  
It highlights the importance of data-driven decision-making in understanding and improving road sa
