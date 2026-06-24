 **🇮🇳 India Census 2011 Interactive Dashboard**

An interactive **Streamlit dashboard** built using the **India Census 2011 district-level dataset**.
This project is designed to explore census data in a more visual and user-friendly way by combining **maps, rankings, comparisons, and category-based analytics**.

It allows users to analyze India or any individual state across multiple dimensions such as **population, literacy, workers, religion, household facilities, education, and housing-related indicators**.

---

## 📌 Project Overview

The main idea of this project is to make a large census dataset easier to explore.

Instead of looking at hundreds of raw columns in a CSV file, this dashboard organizes the data into meaningful categories and gives an interactive interface where users can:

* choose a **state** or view **Overall India**
* select a **category** of census indicators
* compare **primary and secondary parameters**
* see **district-wise maps**
* view **top / bottom districts**
* compare **states**
* explore **religion-based comparisons**
* download filtered data

This project is useful both as a **learning project** and as a **portfolio project** for data analytics / data science / Python dashboard development.

---

# ✨ Features

## 1. India-wise and State-wise Analysis

* View the dashboard for **Overall India**
* Or select a **specific state** to focus only on its districts

## 2. Category-wise Dashboard

Instead of showing 100+ columns together, the dataset is grouped into meaningful sections:

* **Demographics**
* **Social Category**
* **Workers**
* **Religion**
* **Facilities**
* **Education**
* **Housing & Water**

## 3. Interactive District Map

* Districts are shown on a map using **Plotly scatter map**
* **Bubble size** is controlled by the selected primary parameter
* **Bubble color** is controlled by the selected secondary parameter

This makes it easy to spot regional patterns visually.

## 4. KPI Summary Cards

Quick overview metrics are shown at the top of the dashboard, such as:

* Total Population
* Average Literacy Rate
* Average Sex Ratio
* District Count

## 5. Top 5 / Bottom 5 District Rankings

For the selected parameters, the dashboard shows:

* Top 5 districts
* Bottom 5 districts

This helps identify the best / lowest districts for a chosen indicator.

## 6. Top 5 Bar Chart

A bar chart is created for the top districts of the selected primary parameter.

## 7. Distribution Analysis

A histogram is used to show the distribution of the selected metric across districts.

## 8. Primary vs Secondary Scatter Plot

Users can compare two selected parameters and visually inspect their relationship.

## 9. Correlation Heatmap

A category-wise heatmap is included to understand correlations between related census features.

## 10. District Search

Users can directly search and inspect a district from the dataset.

## 11. State Comparison

Two states can be compared using the selected primary metric.

## 12. Religion Comparison

The dashboard also includes religion-based state comparison using major religion columns like:

* Hindus
* Muslims
* Christians
* Sikhs
* Buddhists
* Jains

This can be used to compare either **raw counts** or **percentage share**.

## 13. Download Filtered Data

The filtered dataset currently being used in the dashboard can be downloaded as a CSV file.

---

# 📂 Dataset

**Dataset file used:** `india3.csv`

The dataset contains district-level census information for India and includes features related to:

* Population
* Gender
* Literacy
* SC / ST population
* Workers / Non-workers
* Religion
* Household facilities
* Education levels
* Housing and water-related indicators

---

# 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **Plotly Express**

---

# 📊 Derived Features Added

To make the dashboard more informative, several percentage-based columns were created from the raw dataset.
These derived features help in making comparisons more meaningful.

Some examples:

* `female_percent`
* `male_percent`
* `literacy_percent`
* `worker_percent`
* `non_worker_percent`
* `sc_percent`
* `st_percent`
* `hindu_percent`
* `muslim_percent`
* `christian_percent`
* `internet_percent`
* `electricity_percent`
* `computer_percent`
* `tv_percent`
* `lpg_percent`
* `graduate_percent`
* `higher_education_percent`
* `secondary_education_percent`

---

# 🧩 Dashboard Sections

The dashboard currently includes the following sections:

* **Census Overview**
* **India / State Map**
* **Top / Bottom Rankings**
* **Top 5 Visualization**
* **Distribution Plot**
* **Primary vs Secondary Scatter Plot**
* **Correlation Heatmap**
* **District Search**
* **State Comparison**
* **Religion Comparison**
* **Filtered Data Preview**
* **Download Filtered Data**

---

# 🚀 How to Run the Project

## 1. Clone the repository

```bash
git clone https://github.com/Monu26052006/India-census-dashboard.git
```

## 2. Install dependencies

```bash
pip install streamlit pandas plotly
```

## 3. Make sure the dataset file is present

Keep the following files in the same folder:

* `app.py` *(or your main Python file name)*
* `india3.csv`

## 4. Run the Streamlit app

```bash
streamlit run app.py
```

If your Python file has another name, replace `app.py` with that filename.

---

# 📁 Project Structure

```bash
India-Census-Dashboard/
│
├── app.py
├── india3.csv
├── README.md
└── requirements.txt   # optional
```

---

# 📌 Example Use Cases

This dashboard can be used for:

* district-wise literacy analysis
* population comparison between states
* religion share comparison across states
* worker and non-worker analysis
* internet / electricity / facility analysis
* education-level comparison across regions
* building a portfolio project in Streamlit

---

# 🔮 Possible Future Improvements

Some ideas for improving the project further:

* Add **tabs** for cleaner dashboard navigation
* Add a **Top-N slider** instead of fixed Top 5
* Add **pie charts** for religion and category-wise distributions
* Add **choropleth maps** if district/state geojson data is available
* Add **filters for region / zone**
* Improve **dashboard styling and theme**
* Add **export as image / report**
* Add **more interactive comparisons**

---
# 🎯 Why I Built This Project

I built this project to practice working with a **real-world structured dataset** and to improve my skills in:

* data cleaning
* feature engineering
* exploratory data analysis
* dashboard development with Streamlit
* interactive visualization with Plotly

It also serves as a good **portfolio project** because it combines data processing, analysis, and UI-based presentation in one place.

---

# 🙌 Final Note

This is a learning + portfolio project built around the **India Census 2011** dataset.
The goal was not just to plot charts, but to create a dashboard where the data becomes easier to explore and compare in an interactive way.

If you have suggestions or ideas to improve the dashboard, feel free to extend it further.

---
