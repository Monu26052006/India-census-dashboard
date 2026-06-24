import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="India Census 2011 Dashboard", layout="wide")
df = pd.read_csv("india3.csv")


# Derived percentage columns
df["female_percent"] = round((df["Female"] / df["Population"]) * 100,3)
df["male_percent"] = round((df["Male"] / df["Population"]) * 100,3)
df["literacy_percent"] = round((df["Literate"] / df["Population"]) * 100,3)

df["worker_percent"] = round((df["Workers"] / df["Population"]) * 100,3)
df["non_worker_percent"] = round((df["Non_Workers"] / df["Population"]) * 100,3)
df["main_worker_percent"] = round((df["Main_Workers"] / df["Population"]) * 100,2)
df["marginal_worker_percent"] = round((df["Marginal_Workers"] / df["Population"]) * 100,2)

df["sc_percent"] = round((df["SC"] / df["Population"]) * 100,3)
df["st_percent"] = round((df["ST"] / df["Population"]) * 100,3)

df["hindu_percent"] = round((df["Hindus"] / df["Population"]) * 100,3)
df["muslim_percent"] = round((df["Muslims"] / df["Population"]) * 100,3)
df["christian_percent"] = round((df["Christians"] / df["Population"]) * 100,3)

df["internet_percent"] = round((df["Households_with_Internet"] / df["Households"]) * 100,3)
df["electricity_percent"] = round((df["Housholds_with_Electric_Lighting"] / df["Households"]) * 100,3)
df["computer_percent"] = round((df["Households_with_Computer"] / df["Households"]) * 100,3)
df["tv_percent"] = round((df["Households_with_Television"] / df["Households"]) * 100,3)
df["lpg_percent"] = round((df["LPG_or_PNG_Households"] / df["Households"]) * 100,3)
df["bicycle_percent"] = round((df["Households_with_Bicycle"] / df["Households"]) * 100,3)
df["car_percent"] = round((df["Households_with_Car_Jeep_Van"] / df["Households"]) * 100,3)

df["urban_household_percent"] = round((df["Urban_Households"] / df["Households"]) * 100,3)
df["rural_household_percent"] = round((df["Rural_Households"] / df["Households"]) * 100,3)

df["graduate_percent"] = round((df["Graduate_Education"] / df["Total_Education"]) * 100,3)
df["higher_education_percent"] = round((df["Higher_Education"] / df["Total_Education"]) * 100,3)
df["secondary_education_percent"] = round((df["Secondary_Education"] / df["Total_Education"]) * 100,3)

# Replace
df = df.replace([float("inf"), -float("inf")], pd.NA)
df = df.fillna(0)

# columns groups
demographic_cols = [
    "Population", "Male", "Female", "Literate",
    "Male_Literate", "Female_Literate",
    "sex_ratio", "literacy_rate",
    "female_percent", "male_percent", "literacy_percent",
    "Age_Group_0_29", "Age_Group_30_49", "Age_Group_50"
]

social_cols = [
    "SC", "Male_SC", "Female_SC",
    "ST", "Male_ST", "Female_ST",
    "sc_percent", "st_percent"
]

worker_cols = [
    "Workers", "Male_Workers", "Female_Workers",
    "Main_Workers", "Marginal_Workers", "Non_Workers",
    "Cultivator_Workers", "Agricultural_Workers",
    "Household_Workers", "Other_Workers",
    "worker_percent", "non_worker_percent",
    "main_worker_percent", "marginal_worker_percent"
]

religion_cols = [
    "Hindus", "Muslims", "Christians", "Sikhs",
    "Buddhists", "Jains", "Others_Religions",
    "Religion_Not_Stated",
    "hindu_percent", "muslim_percent", "christian_percent"
]

facility_cols = [
    "Households", "Rural_Households", "Urban_Households",
    "LPG_or_PNG_Households",
    "Housholds_with_Electric_Lighting",
    "Households_with_Internet",
    "Households_with_Computer",
    "Households_with_Bicycle",
    "Households_with_Car_Jeep_Van",
    "Households_with_Television",
    "internet_percent", "electricity_percent",
    "computer_percent", "tv_percent", "lpg_percent",
    "bicycle_percent", "car_percent",
    "urban_household_percent", "rural_household_percent"
]

education_cols = [
    "Below_Primary_Education", "Primary_Education",
    "Middle_Education", "Secondary_Education",
    "Higher_Education", "Graduate_Education",
    "Other_Education", "Literate_Education",
    "Illiterate_Education", "Total_Education",
    "graduate_percent", "higher_education_percent",
    "secondary_education_percent"
]

housing_cols = [
    "Having_bathing_facility_Total_Households",
    "Having_latrine_facility_within_the_premises_Total_Households",
    "Ownership_Owned_Households",
    "Ownership_Rented_Households",
    "Households_with_separate_kitchen_Cooking_inside_house",
    "Condition_of_occupied_census_houses_Dilapidated_Households",
    "Not_having_bathing_facility_within_the_premises_Total_Households",
    "Location_of_drinking_water_source_Within_the_premises_Households",
    "Location_of_drinking_water_source_Near_the_premises_Households",
    "Location_of_drinking_water_source_Away_Households",
    "Main_source_of_drinking_water_Tapwater_Households",
    "Main_source_of_drinking_water_Tubewell_Borehole_Households"
]

category_dict = {
    "Demographics": demographic_cols,
    "Social Category": social_cols,
    "Workers": worker_cols,
    "Religion": religion_cols,
    "Facilities": facility_cols,
    "Education": education_cols,
    "Housing & Water": housing_cols
}

# sIDEBAR
st.sidebar.title("India Census 2011 Dashboard")

list_of_states = ["Overall India"] + sorted(df["State"].unique().tolist())

selected_state = st.sidebar.selectbox("Select a State", list_of_states)

selected_category = st.sidebar.selectbox(
    "Select Category",
    list(category_dict.keys())
)

available_cols = category_dict[selected_category]

primary = st.sidebar.selectbox("Select Primary Parameter", available_cols)
secondary = st.sidebar.selectbox("Select Secondary Parameter", available_cols)

plot = st.sidebar.button("Plot Graph")


# FILTERED
if selected_state == "Overall India":
    temp_df = df.copy()
    zoom_level = 4
else:
    temp_df = df[df["State"] == selected_state].copy()
    zoom_level = 6


# TITLE
st.title("🇮🇳 India Census 2011 Interactive Dashboard")
st.caption("Built from india3.csv with category-wise analysis, maps, rankings, and comparisons.")

# KPI
st.markdown("##  Census Overview")

if selected_state == "Overall India":
    total_population = temp_df["Population"].sum()
    avg_literacy = temp_df["literacy_rate"].mean()
    avg_sex_ratio = temp_df["sex_ratio"].mean()
else:
    total_population = temp_df["Population"].sum()
    avg_literacy = temp_df["literacy_rate"].mean()
    avg_sex_ratio = temp_df["sex_ratio"].mean()

k1, k2, k3, k4 = st.columns(4)
k1.metric("Total Population", f"{total_population:,.0f}")
k2.metric("Average Literacy Rate", f"{avg_literacy:.2f}%")
k3.metric("Average Sex Ratio", f"{avg_sex_ratio:.2f}")
k4.metric("District Count", f"{temp_df['District'].nunique()}")


# MAP
st.markdown("##  India / State Map")

if plot:
    fig = px.scatter_mapbox(
        temp_df,
        lat="Latitude",
        lon="Longitude",
        size=primary,
        color=secondary,
        color_continuous_scale="Turbo",
        zoom=zoom_level,
        size_max=35,
        mapbox_style="carto-positron",
        width=1200,
        height=700,
        hover_name="District",
        hover_data={
            "State": True,
            primary: True,
            secondary: True,
            "Latitude": False,
            "Longitude": False
        }
    )
    st.plotly_chart(fig, use_container_width=True)


# TOP / BOTTOM RANKINGS
st.markdown("## Rankings")

r1, r2 = st.columns(2)

with r1:
    st.subheader(f"Top 5 by {primary}")
    if selected_state == "Overall India":
        top5_primary = temp_df.nlargest(5, primary)[["State", "District", primary]]
    else:
        top5_primary = temp_df.nlargest(5, primary)[["District", primary]]
    st.dataframe(top5_primary, use_container_width=True)

with r2:
    st.subheader(f"Bottom 5 by {primary}")
    if selected_state == "Overall India":
        bottom5_primary = temp_df.nsmallest(5, primary)[["State", "District", primary]]
    else:
        bottom5_primary = temp_df.nsmallest(5, primary)[["District", primary]]
    st.dataframe(bottom5_primary, use_container_width=True)

r3, r4 = st.columns(2)

with r3:
    st.subheader(f"Top 5 by {secondary}")
    if selected_state == "Overall India":
        top5_secondary = temp_df.nlargest(5, secondary)[["State", "District", secondary]]
    else:
        top5_secondary = temp_df.nlargest(5, secondary)[["District", secondary]]
    st.dataframe(top5_secondary, use_container_width=True)

with r4:
    st.subheader(f"Bottom 5 by {secondary}")
    if selected_state == "Overall India":
        bottom5_secondary = temp_df.nsmallest(5, secondary)[["State", "District", secondary]]
    else:
        bottom5_secondary = temp_df.nsmallest(5, secondary)[["District", secondary]]
    st.dataframe(bottom5_secondary, use_container_width=True)


# TOP 5 BAR CHART

st.markdown("##  Top 5 Visualization")

fig_bar = px.bar(
    top5_primary,
    x="District",
    y=primary,
    color=top5_primary.columns[0] if selected_state == "Overall India" else None,
    title=f"Top 5 Districts by {primary}"
)
st.plotly_chart(fig_bar, use_container_width=True)
# HISTOGRAM
st.markdown("##  Distribution")

fig_hist = px.histogram(
    temp_df,
    x=primary,
    nbins=30,
    title=f"Distribution of {primary}"
)
st.plotly_chart(fig_hist, use_container_width=True)

# SCATTER PLOT
st.markdown("##  Primary vs Secondary")

fig_scatter = px.scatter(
    temp_df,
    x=primary,
    y=secondary,
    hover_name="District",
    color="State",
    title=f"{primary} vs {secondary}"
)
st.plotly_chart(fig_scatter, use_container_width=True)
# CORRELATION HEATMAP
st.markdown("##  Correlation Heatmap")

numeric_cols = temp_df.select_dtypes(include="number").columns.tolist()
exclude_cols = ["Latitude", "Longitude", "District code"]
numeric_cols = [c for c in numeric_cols if c not in exclude_cols]

# Keep heatmap readable by using current category columns only

heatmap_cols = [c for c in available_cols if c in numeric_cols]
if len(heatmap_cols) >= 2:
    corr = temp_df[heatmap_cols].corr()
    fig_heat = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        title=f"Correlation Heatmap - {selected_category}"
    )
    st.plotly_chart(fig_heat, use_container_width=True)
else:
    st.info("Not enough numeric columns in this category for a heatmap.")

#district
st.markdown("##  Search District")

district = st.selectbox(
    "Select District",
    sorted(df["District"].unique())
)

district_data = df[df["District"] == district]
st.dataframe(district_data, use_container_width=True)

# STATE COMPARISON

st.markdown("## State Comparison")

c1, c2 = st.columns(2)

with c1:
    state1 = st.selectbox("State 1", sorted(df["State"].unique()), key="state1")
with c2:
    state2 = st.selectbox("State 2", sorted(df["State"].unique()), index=1, key="state2")

compare_df = df.groupby("State")[primary].sum().reset_index()

fig_compare = px.bar(
    compare_df[compare_df["State"].isin([state1, state2])],
    x="State",
    y=primary,
    color="State",
    title=f"{primary} Comparison: {state1} vs {state2}"
)
st.plotly_chart(fig_compare, use_container_width=True)

#  PREVIEW

st.markdown("##  Filtered Data Preview")
st.dataframe(temp_df.head(20), use_container_width=True)

# DOWNLOAD

st.markdown("##  Download Filtered Data")

csv = temp_df.to_csv(index=False)

st.download_button(
    label="Download Filtered CSV",
    data=csv,
    file_name="filtered_india_census.csv",
    mime="text/csv"
)

